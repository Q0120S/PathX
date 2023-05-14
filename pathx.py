from urllib.parse import urlparse
import argparse

def append_string_to_path(url, string):
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.split('/')
    result_urls = []
    for i in range(2, len(path_segments)+1):
        if i == len(path_segments):
            new_path = '/'.join(path_segments[:i]) + string + '/'.join(path_segments[i:])
        else:
            new_path = '/'.join(path_segments[:i]) + string + '/' + '/'.join(path_segments[i:])

        new_url = parsed_url.scheme + '://' + parsed_url.netloc + new_path       
        result_urls.append(new_url)
        
    return result_urls

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Appending string in different ways to a URL path.')
    parser.add_argument('-u', '--url', type=str, help='target URL to modify')
    parser.add_argument('-s', '--string', type=str, help='string to append to the URL path')
    args = parser.parse_args()

    if not args.url or not args.string:
        print("Please provide both a URL and string to append to the path.")
    else:
        result_urls = append_string_to_path(args.url, args.string)
        for url in result_urls:
            print(url)
