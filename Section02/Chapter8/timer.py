def timer():
        import time
        hours = 0  
        while hours < 2:
            for hours in range(0,24):
                for minutes in range(0, 60):
                    for seconds in range(0, 60):
                        time.sleep(1)
                        print(hours,":", minutes,":", seconds)
timer()
