from re import A
from url_creator.models import ShortenedUrlPath
from url_creator.shortened_url_generator import generate_url_paths
from itertools import islice

def require_more_url_paths():
    return number_of_available_urls() < 50

def number_of_available_urls():
    return ShortenedUrlPath.objects.filter(in_use=False).count()

def add_new_available_paths(count):
    url_paths = generate_url_paths(count)
    current_available_paths = ShortenedUrlPath.objects.filter(in_use=False)
    for object in current_available_paths:
        if object.shortened_url_path in url_paths:
            url_paths.remove(object.shortened_url_path)

    deduplicated_url_path_entries = []

    for url_path in url_paths:
        url_path_entry = ShortenedUrlPath(shortened_url_path=url_path, in_use=False)
        deduplicated_url_path_entries.append(url_path_entry)
        url_path_entry.save()

    # batch_size = 10

    # while True:
    #     batch = list(islice(deduplicated_url_path_entries, batch_size))
    #     if not batch:
    #         break
    #     ShortenedUrlPath.objects.bulk_create(batch, batch_size)

def get_available_shortened_url_path():
    entry = ShortenedUrlPath.objects.filter(in_use=False).first()
    entry.in_use = True
    entry.save()
    return entry.shortened_url_path