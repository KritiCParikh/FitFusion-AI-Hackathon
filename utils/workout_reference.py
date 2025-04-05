from tavily import TavilyClient
import os
from config import HUGGINGFACE_API_KEY

class WorkoutReference:
    def __init__(self):
        self.tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
        
    def get_exercise_references(self, exercise_name):
        try:
            # Search for exercise form videos and GIFs
            query = f"{exercise_name} proper form tutorial video or gif"
            response = self.tavily_client.search(
                query,
                search_depth="advanced",
                include_answer=True,
                include_raw_content=True
            )
            
            # Filter and format the results
            references = []
            for result in response.get('results', []):
                if any(ext in result.get('url', '').lower() for ext in ['.gif', '.mp4', 'youtube.com', 'vimeo.com']):
                    references.append({
                        'title': result.get('title', ''),
                        'url': result.get('url', ''),
                        'content': result.get('content', '')
                    })
            
            return references[:3]  # Return top 3 references
        except Exception as e:
            print(f"Error getting exercise references: {str(e)}")
            return [] 