def domain_name(url: str) -> str:
    url = url.replace("https://", "").replace("http://", "").replace("www.", '').replace("https://www.", "").replace(
        "http://www.", "").split('.')
    return url[0]

