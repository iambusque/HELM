#!/usr/bin/env python3
"""
Weekly AM Notes Collection Service
Automatically collects and organizes Account Manager call notes from Confluence

This script uses the same MCP Atlassian integration patterns used in the manual collection.
It's designed to run weekly and automatically organize AM call notes in the HELM vault.
"""

import os
import json
import yaml
from datetime import datetime, timedelta
from pathlib import Path
import logging
import re
from typing import Dict, List, Optional, Tuple

# Configure logging
def setup_logging():
    log_dir = Path("service/logs")
    log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_dir / 'am_collection.log'),
            logging.StreamHandler()
        ]
    )

class AMNotesCollector:
    def __init__(self, config_path="service/weekly_collection_config.yaml"):
        """Initialize the AM Notes Collector"""
        setup_logging()
        self.config = self.load_config(config_path)
        self.base_path = Path(self.config['output']['base_path'])
        self.setup_directories()
        
        # AM name mapping for content parsing
        self.am_mapping = self._build_am_mapping()
        
    def load_config(self, config_path: str) -> dict:
        """Load configuration from YAML file"""
        try:
            with open(config_path, 'r') as file:
                config = yaml.safe_load(file)
                logging.info(f"Loaded configuration from {config_path}")
                return config
        except Exception as e:
            logging.error(f"Failed to load config: {e}")
            raise
    
    def _build_am_mapping(self) -> Dict[str, List[str]]:
        """Build mapping of AM names and their variations"""
        mapping = {}
        all_ams = (
            self.config['account_managers']['primary_sales'] +
            self.config['account_managers']['regional'] +
            self.config['account_managers']['client_services']
        )
        
        for am in all_ams:
            # Add full name and variations
            variations = [am]
            if ' ' in am:
                first_name = am.split()[0]
                variations.append(first_name)
            mapping[am] = variations
            
        return mapping
    
    def setup_directories(self):
        """Create necessary directories"""
        self.base_path.mkdir(exist_ok=True)
        
        # Create service directories
        service_dir = self.base_path / "service"
        service_dir.mkdir(exist_ok=True)
        (service_dir / "logs").mkdir(exist_ok=True)
        
        # Create AM folders
        all_ams = (
            self.config['account_managers']['primary_sales'] +
            self.config['account_managers']['regional'] +
            self.config['account_managers']['client_services']
        )
        
        for am in all_ams:
            am_dir = self.base_path / am
            am_dir.mkdir(exist_ok=True)
            logging.debug(f"Ensured directory exists: {am_dir}")
    
    def get_date_range(self) -> Tuple[str, str]:
        """Get the date range for the previous week (Monday to Sunday)"""
        today = datetime.now()
        # Get last Monday
        days_since_monday = today.weekday()
        last_monday = today - timedelta(days=days_since_monday + 7)
        last_sunday = last_monday + timedelta(days=6)
        
        start_date = last_monday.strftime("%Y-%m-%d")
        end_date = last_sunday.strftime("%Y-%m-%d")
        
        logging.info(f"Collection period: {start_date} to {end_date}")
        return start_date, end_date
    
    def search_confluence_notes(self, start_date: str, end_date: str) -> List[dict]:
        """
        Search for call notes and daily digests in date range using MCP Atlassian tools
        """
        notes_data = []
        
        try:
            # Get MCP configuration from environment or config
            cloud_id = os.getenv('MCP_ATLASSIAN_CLOUD_ID', '05fe7108-c795-4295-8062-b43ad1f2e363')
            base_url = os.getenv('MCP_ATLASSIAN_BASE_URL', 'https://edocgroup.atlassian.net')
            
            logging.info(f"Searching Confluence using MCP tools for date range: {start_date} to {end_date}")
            
            # Search for call notes in SAL space
            call_notes_cql = f'space = "SAL" AND (title ~ "call notes" OR title ~ "Call Notes") AND lastModified >= "{start_date}" AND lastModified <= "{end_date + " 23:59:59"}"'
            logging.info(f"Call notes CQL: {call_notes_cql}")
            
            # In production, this would use:
            # call_results = mcp_atlassian_searchConfluenceUsingCql(
            #     cloudId=cloud_id, 
            #     cql=call_notes_cql,
            #     limit=self.config['search_config']['max_results_per_search']
            # )
            
            # Search for daily digests in CS space  
            digest_cql = f'space = "CS" AND title ~ "Daily Digest" AND lastModified >= "{start_date}" AND lastModified <= "{end_date + " 23:59:59"}"'
            logging.info(f"Daily digest CQL: {digest_cql}")
            
            # In production, this would use:
            # digest_results = mcp_atlassian_searchConfluenceUsingCql(
            #     cloudId=cloud_id,
            #     cql=digest_cql, 
            #     limit=self.config['search_config']['max_results_per_search']
            # )
            
            # For each result, get full content:
            # for result in call_results + digest_results:
            #     page_content = mcp_atlassian_getConfluencePage(
            #         cloudId=cloud_id,
            #         pageId=result['id']
            #     )
            #     notes_data.append({
            #         'title': result['title'],
            #         'date': result['lastModified'][:10],  # Extract date
            #         'content': page_content['body'],
            #         'attendees': self._extract_attendees(page_content['body']),
            #         'recording': self._extract_recording_link(page_content['body']),
            #         'page_id': result['id']
            #     })
            
            logging.warning("MCP integration template - replace with actual mcp_atlassian_* tool calls")
            logging.info(f"Would search for notes between {start_date} and {end_date} using cloud_id: {cloud_id}")
            
        except Exception as e:
            logging.error(f"Error searching Confluence via MCP: {e}")
            
        return notes_data
    
    def _extract_attendees(self, content: str) -> str:
        """Extract attendees from page content"""
        # Look for common patterns like "Attendees:", "Present:", etc.
        patterns = [
            r'attendees?:?\s*([^\n\r]+)',
            r'present:?\s*([^\n\r]+)', 
            r'participants?:?\s*([^\n\r]+)'
        ]
        
        for pattern in patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return ""
    
    def _extract_recording_link(self, content: str) -> str:
        """Extract recording link from page content"""
        # Look for recording URLs
        recording_patterns = [
            r'recording:?\s*(https?://[^\s\)]+)',
            r'(https?://[^\s]*zoom[^\s]*)',
            r'(https?://[^\s]*teams[^\s]*)',
            r'(https?://[^\s]*meet[^\s]*)'
        ]
        
        for pattern in recording_patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        return ""
    
    def extract_am_name(self, note: dict) -> Optional[str]:
        """Extract Account Manager name from note data"""
        # Check attendees field
        attendees = note.get('attendees', '')
        for am_name, variations in self.am_mapping.items():
            for variation in variations:
                if variation.lower() in attendees.lower():
                    return am_name
        
        # Check title
        title = note.get('title', '')
        for am_name, variations in self.am_mapping.items():
            for variation in variations:
                if variation.lower() in title.lower():
                    return am_name
        
        # Check content
        content = note.get('content', '')
        for am_name, variations in self.am_mapping.items():
            for variation in variations:
                if variation.lower() in content.lower():
                    return am_name
        
        return None
    
    def organize_notes_by_am(self, notes_data: List[dict]) -> Dict[str, List[dict]]:
        """Organize collected notes by Account Manager"""
        organized_notes = {}
        unassigned_notes = []
        
        for note in notes_data:
            am_name = self.extract_am_name(note)
            if am_name:
                if am_name not in organized_notes:
                    organized_notes[am_name] = []
                organized_notes[am_name].append(note)
                logging.debug(f"Assigned note '{note.get('title', 'Unknown')}' to {am_name}")
            else:
                unassigned_notes.append(note)
                logging.warning(f"Could not assign note: {note.get('title', 'Unknown')}")
        
        if unassigned_notes:
            logging.warning(f"Found {len(unassigned_notes)} unassigned notes")
        
        return organized_notes
    
    def format_am_notes(self, am_name: str, notes: List[dict], start_date: str, end_date: str) -> str:
        """Format notes into markdown"""
        content = f"# {am_name} - Call Notes ({start_date} to {end_date})\\n\\n"
        
        if not notes:
            content += "No call notes found for this period.\\n"
            return content
        
        # Sort notes by date
        sorted_notes = sorted(notes, key=lambda x: x.get('date', ''), reverse=True)
        
        for note in sorted_notes:
            content += f"## {note.get('title', 'Untitled Note')}\\n"
            content += f"**Date:** {note.get('date', 'Unknown')}\\n"
            
            attendees = note.get('attendees', '')
            if attendees:
                content += f"**Attendees:** {attendees}\\n"
            
            if note.get('recording'):
                content += f"**Recording:** {note['recording']}\\n"
            
            content += "\\n"
            
            # Add note content
            note_content = note.get('content', '')
            if note_content:
                content += note_content + "\\n"
            
            content += "\\n---\\n\\n"
        
        return content
    
    def generate_am_files(self, organized_notes: Dict[str, List[dict]], start_date: str, end_date: str):
        """Generate markdown files for each AM"""
        generated_files = []
        
        for am_name, notes in organized_notes.items():
            filename = f"Call_Notes_{start_date}_to_{end_date}.md"
            filepath = self.base_path / am_name / filename
            
            content = self.format_am_notes(am_name, notes, start_date, end_date)
            
            try:
                with open(filepath, 'w', encoding='utf-8') as file:
                    file.write(content)
                
                generated_files.append(filepath)
                logging.info(f"Generated: {filepath}")
                
            except Exception as e:
                logging.error(f"Failed to write {filepath}: {e}")
        
        return generated_files
    
    def generate_summary_report(self, organized_notes: Dict[str, List[dict]], start_date: str, end_date: str) -> Path:
        """Generate cross-AM summary report"""
        filename = f"AM_Notes_Summary_{start_date}_to_{end_date}.md"
        filepath = self.base_path / filename
        
        # Count total notes and active AMs
        total_notes = sum(len(notes) for notes in organized_notes.values())
        active_ams = len([am for am, notes in organized_notes.items() if notes])
        
        content = f"# AM Call Notes Summary - Week of {start_date} to {end_date}\\n\\n"
        content += f"## Collection Summary\\n"
        content += f"**Period:** {start_date} to {end_date}\\n"
        content += f"**Total Notes Collected:** {total_notes}\\n"
        content += f"**Active AMs:** {active_ams}\\n\\n"
        
        content += "## Notes by Account Manager\\n\\n"
        
        for am_name, notes in sorted(organized_notes.items()):
            if notes:
                content += f"### {am_name} ✅\\n"
                content += f"- **{len(notes)} notes** collected\\n"
                for note in notes:
                    content += f"  - {note.get('title', 'Untitled')} ({note.get('date', 'Unknown date')})\\n"
                content += "\\n"
        
        # List AMs with no activity
        all_ams = (
            self.config['account_managers']['primary_sales'] +
            self.config['account_managers']['regional'] +
            self.config['account_managers']['client_services']
        )
        
        inactive_ams = [am for am in all_ams if am not in organized_notes or not organized_notes[am]]
        
        if inactive_ams:
            content += "## AMs with No Recent Activity\\n\\n"
            for am in inactive_ams:
                content += f"- {am}\\n"
            content += "\\n"
        
        content += f"---\\n\\n"
        content += f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n"
        content += f"**Source:** Confluence SAL and CS spaces\\n"
        
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
            
            logging.info(f"Generated summary: {filepath}")
            return filepath
            
        except Exception as e:
            logging.error(f"Failed to write summary {filepath}: {e}")
            raise
    
    def archive_previous_week(self):
        """Archive previous week's files if enabled"""
        if not self.config['output']['archive_previous']:
            return
        
        logging.info("Archiving previous week's files...")
        
        # Create archive directory
        archive_dir = self.base_path / "archive" / datetime.now().strftime("%Y")
        archive_dir.mkdir(parents=True, exist_ok=True)
        
        # Archive summary files older than 7 days
        for summary_file in self.base_path.glob("AM_Notes_Summary_*.md"):
            if summary_file.stat().st_mtime < (datetime.now() - timedelta(days=7)).timestamp():
                archive_path = archive_dir / summary_file.name
                summary_file.rename(archive_path)
                logging.info(f"Archived: {summary_file} -> {archive_path}")
    
    def send_notification(self, summary_data: Dict):
        """Send completion notification"""
        if not self.config['notifications']['enabled']:
            return
        
        # This would implement email notification
        # Could use SMTP, SendGrid, or other email service
        logging.info("Notifications not implemented - would send email summary")
    
    def run_collection(self) -> Dict:
        """Main collection process"""
        start_time = datetime.now()
        
        try:
            logging.info("="*60)
            logging.info("Starting weekly AM notes collection")
            logging.info("="*60)
            
            # Get date range
            start_date, end_date = self.get_date_range()
            
            # Archive previous week if enabled
            self.archive_previous_week()
            
            # Search for notes (would use MCP tools in production)
            notes_data = self.search_confluence_notes(start_date, end_date)
            logging.info(f"Found {len(notes_data)} total notes")
            
            # Organize by AM
            organized_notes = self.organize_notes_by_am(notes_data)
            active_ams = len([am for am, notes in organized_notes.items() if notes])
            logging.info(f"Organized notes for {active_ams} active AMs")
            
            # Generate AM files
            generated_files = self.generate_am_files(organized_notes, start_date, end_date)
            
            # Generate summary
            summary_file = self.generate_summary_report(organized_notes, start_date, end_date)
            
            # Prepare results
            results = {
                'success': True,
                'start_date': start_date,
                'end_date': end_date,
                'total_notes': sum(len(notes) for notes in organized_notes.values()),
                'active_ams': active_ams,
                'generated_files': [str(f) for f in generated_files],
                'summary_file': str(summary_file),
                'execution_time': (datetime.now() - start_time).total_seconds()
            }
            
            # Send notification
            self.send_notification(results)
            
            logging.info("="*60)
            logging.info(f"Weekly collection completed successfully in {results['execution_time']:.1f} seconds")
            logging.info(f"Generated {len(generated_files)} AM files and 1 summary file")
            logging.info("="*60)
            
            return results
            
        except Exception as e:
            logging.error("="*60)
            logging.error(f"Collection failed: {str(e)}")
            logging.error("="*60)
            
            return {
                'success': False,
                'error': str(e),
                'execution_time': (datetime.now() - start_time).total_seconds()
            }

def main():
    """Main entry point"""
    try:
        # Change to script directory
        script_dir = Path(__file__).parent.parent
        os.chdir(script_dir)
        
        # Run collection
        collector = AMNotesCollector()
        results = collector.run_collection()
        
        # Exit with appropriate code
        exit_code = 0 if results['success'] else 1
        exit(exit_code)
        
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        exit(1)

if __name__ == "__main__":
    main()