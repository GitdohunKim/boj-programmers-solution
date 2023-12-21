def solution(routes):
    routes.sort(key=lambda x: x[1])  
    camera_count = 1  
    current_camera = routes[0][1]  

    for route in routes:
        if route[0] > current_camera:
            camera_count += 1
            current_camera = route[1]

    return camera_count
