def mobile(request):
    """
    Indicates if the user is viewing the site on his mobile device or not
    """
    AGENTS = ['iphone', 'ipad', 'android', 'blackberry', 'windows phone os 7', 'iemobile']

    mobile = False
    ua = request.META.get('HTTP_USER_AGENT', '').lower()
    for agent in AGENTS:
        if agent in ua:
            mobile = True
    return {'mobile': mobile}