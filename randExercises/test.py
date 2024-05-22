results = []
    for username in usernames:
        if any(username[i] > username[i + 1] for i in range(len(username) - 1)):
            results.append("YES")
        else:
            results.append("NO")
    return results
