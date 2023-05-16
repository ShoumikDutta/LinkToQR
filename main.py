import qrcode


def main():
    img = qrcode.make(input("Link: "))
    type(img) 
    img.save(input("File Name: ")+".png")

if __name__=="__main__":
    main()
