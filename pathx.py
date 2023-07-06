from urllib.parse import urlparse
import argparse
import sys

def append_string_to_path(url, string, no_ending_slash=False):
    parsed_url = urlparse(url)
    if parsed_url.path != '/':
        path = parsed_url.path + '/'    
    else:
        path = parsed_url.path
    
    path_segments = path.split('/')
    result_urls = set()
    for i in range(2, len(path_segments)+1):
        if i == len(path_segments):
            new_path = '/'.join(path_segments[:i]) + string 
        else:
            new_path = '/'.join(path_segments[:i]) + string + '/' + '/'.join(path_segments[i:])

        if parsed_url.query != '':
            new_url = parsed_url.scheme + '://' + parsed_url.netloc + new_path + '?' + parsed_url.query
        else:
            new_url = parsed_url.scheme + '://' + parsed_url.netloc + new_path
        
        result_urls.add(new_url)
    
    for i in range(1, len(path_segments)+1):
        if i == len(path_segments):
            new_path = '/'.join(path_segments[:i]) + string 
        else:
            new_path = '/'.join(path_segments[:i]) + '/' + string + '/' + '/'.join(path_segments[i:]) 
        
        if parsed_url.query != '':
            new_url = parsed_url.scheme + '://' + parsed_url.netloc + new_path + '?' + parsed_url.query
        else:
            new_url = parsed_url.scheme + '://' + parsed_url.netloc + new_path 
        
        result_urls.add(new_url) 

    output_urls = []
    for url in result_urls:
        if no_ending_slash and url.endswith('/'):
            output_urls.append(url[:-1])
        else:
            output_urls.append(url)
        
    return output_urls


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Appending string in different ways to a URL path.')
    parser.add_argument('-u', '--url', type=str, help='single target URL.')
    parser.add_argument('-l', '--list', type=str, help='target URL file.')
    parser.add_argument('-s', '--string', type=str, help='string to append to the URL path.')
    parser.add_argument('-ne', '--no-ending-slash', action='store_true', help='omit ending slash from URLs')
    args = parser.parse_args()

    if not args.list and not args.url or not args.string:
        print('Please provide both a URL and string to append to the path.')
    elif args.list:
        seen_urls = set()
        with open(args.list) as input_file:
            for url in input_file.readlines():
                result_urls = append_string_to_path(url.rstrip(), args.string, args.no_ending_slash)
                for new_url in result_urls:
                    if new_url not in seen_urls:
                        seen_urls.add(new_url)
                        print(new_url)
    else:
        result_urls = append_string_to_path(args.url, args.string, args.no_ending_slash)
        seen_urls = set()
        for new_url in result_urls:
            if new_url not in seen_urls:
                seen_urls.add(new_url)
                print(new_url)
