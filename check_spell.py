import urllib
def read_text():
    quotes = open(r"C:\Users\aman5\Desktop\My Python Projects\sample.txt")
    content_of_file = quotes.read()
    print(content_of_file)
    quotes.close()
    check_profanity(content_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()
