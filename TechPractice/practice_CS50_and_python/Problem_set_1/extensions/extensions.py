U = input("Enter file name: ")
V = U.lower().strip().split(".")
match V[-1]:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/"+V[0])
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")