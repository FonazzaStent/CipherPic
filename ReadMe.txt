CypherPic 1.0.0
Fonazza-Stent 2024
Encrypt and decrypt an image

The program can encrypt an image, save it to a file, then decrypt
and display it.
For now it’s a console program (no GUI) composed of two modules,
one for encryption, one for decryption.

ENCODE:

Start the CipherPic_encode module by double-clicking on the program
icon.
You will be prompted for an existing image filename, better if
located in the same folder as the program or you will have to enter
the whole path. Input your image filename and press Enter.

At the prompt “Encoded image filename”, input the filename you want
to assign to your encrypted image. The file may have any or no
extension.

At the prompt “Password”, input a number of any length. This will be
the key you have to remember when decrypting the image. Only numbers
are accepted, no letters, no symbols. Press Enter and wait for the
program to finish encoding the image. You will find your encoded
image in the same folder as the program with the filename you
assigned to it.

DECODE AND DISPLAY:

Start the CipherPic_decode module by double-clicking on the program
icon.
At the prompt “Encrypted image filename” input the filename of the
encrypted image. Better if in the same folder as the program, or you
will have to input the whole path.

At the prompt “Password” input the number you have used to encrypt
the image.

If the number key is correct, the image will be displayed. For now
there’s a limitation, it will only display an 800 pixel height
image. I plan to work on this limitation in future versions.

The program will not save the password anywhere so there’s no way to
retrieve it once you’ve entered it, and you have to remember it 
correctly in order to decrypt the image.
