#Given name of a file, output media type using file extension

#Psuedo code:
#Prompt for file name
#Look for series of characters following "."
#Match characters to media type
#Output media type
file = input("File name: ")
extension = file.split(sep = ".")[1]

match extension:
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")