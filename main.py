# from stegano import lsb

# secret = lsb.hide("img/1.png", "My password: 123")
# secret.save("img/1_secret.png")

# result = lsb.reveal("img/1_secret.png")
# print(result)

# from stegano import exifHeader

# secret = exifHeader.hide("img/2.jpg", "img/2_sec.jpg", "Жду завтра в 8.")

# result = exifHeader.reveal("img/2_sec.jpg").decode()
# print(result)


from steganocryptopy.steganography import Steganography

Steganography.generate_key("")
secret = Steganography.encrypt("key.key", "img/3.jpg", "secret_message.txt")
secret.save("img/3_sec.jpg")

result = Steganography.decrypt("key.key", "img/3_sec.jpg")
print(result)