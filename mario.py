def main():
    height = input("Heigth: ")
    height = int(height)
    while (height < 0 or height > 23):
        height = input("Height: ")
        height = int(height)
    for i in range(1, height + 1):
        for j in range(1, height + 1):
            if j <= height - i:
                print (" ", end = "")
            else:
                print ("#", end = "")
        print("  ", end = "");
        for n in range(1, i+1):
            print("#", end = "")
        print (" ")
        
    
main()