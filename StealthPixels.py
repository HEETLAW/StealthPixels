
from PIL import Image

class ImageEncryptor:
    def __init__(self):
        self.input_image = None
        self.key = None

    def load_image(self, image_path):
        try:
            self.input_image = Image.open(image_path)
            print("Image loaded successfully!")
        except FileNotFoundError:
            print("Error: Image file not found.")
        except Exception as e:
            print(f"An error occurred while loading the image: {e}")

    def encrypt_image(self, output_path):
        if self.input_image is None:
            print("Error: No input image loaded.")
            return

        if self.key is None:
            print("Error: Encryption key not set.")
            return

        width, height = self.input_image.size
        encrypted_image = Image.new("RGB", (width, height))
        pixels = self.input_image.load()

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r = (r + self.key) % 256
                g = (g + self.key) % 256
                b = (b + self.key) % 256
                encrypted_image.putpixel((x, y), (r, g, b))

        encrypted_image.save(output_path)
        print("Image encrypted successfully!")

    def decrypt_image(self, input_path, output_path):
        try:
            encrypted_image = Image.open(input_path)
        except FileNotFoundError:
            print("Error: Encrypted image file not found.")
            return
        except Exception as e:
            print(f"An error occurred while loading the encrypted image: {e}")
            return

        if self.key is None:
            print("Error: Encryption key not set.")
            return

        width, height = encrypted_image.size
        decrypted_image = Image.new("RGB", (width, height))
        pixels = encrypted_image.load()

        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                r = (r - self.key) % 256
                g = (g - self.key) % 256
                b = (b - self.key) % 256
                decrypted_image.putpixel((x, y), (r, g, b))

        decrypted_image.save(output_path)
        print("Image decrypted successfully!")

    def set_key(self, key):
        if not (0 <= key <= 255):
            print("Error: Key must be between 0 and 255.")
            return
        self.key = key

def main():
    encryptor = ImageEncryptor()

    while True:
        print("\n===== Image Encryption Tool =====")
        print("1. Load Image")
        print("2. Set Encryption Key")
        print("3. Encrypt Image")
        print("4. Decrypt Image")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            image_path = input("Enter the path of the image to load: ")
            encryptor.load_image(image_path)
        elif choice == '2':
            try:
                key = int(input("Enter the encryption key (0-255): "))
                encryptor.set_key(key)
            except ValueError:
                print("Error: Key must be an integer.")
        elif choice == '3':
            if encryptor.input_image is None:
                print("Error: No input image loaded.")
            else:
                output_path = input("Enter the output path for encrypted image: ")
                encryptor.encrypt_image(output_path)
        elif choice == '4':
            input_path = input("Enter the path of the encrypted image: ")
            output_path = input("Enter the output path for decrypted image: ")
            encryptor.decrypt_image(input_path, output_path)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
