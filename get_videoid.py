from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    parsed_url = urlparse(url)
    if 'youtube.com' in parsed_url.hostname:
        if '/shorts/' in parsed_url.path:
            return parsed_url.path.split('/')[-1]
        elif 'watch' in parsed_url.path:
            query_params = parse_qs(parsed_url.query)
            return query_params.get('v', [None])[0]
    elif 'youtu.be' in parsed_url.hostname:
        return parsed_url.path[1:]
    return None
