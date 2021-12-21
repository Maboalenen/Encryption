RSA_Encryption
==========

RSA
-----

> first published by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977, RSA implements a public-key cryptosystem, as well as digital signatures

 * Public-key encryption
> In RSA, encryption keys are public, while the decryption keys are not, so only the person with the correct decryption key can decipher an encrypted message.

* Digital signatures.
The receiver may need to verify that a transmitted message actually originated from the sender (signature)This is done using the sender’s decryption key, and the signature can later be verified by anyone, using the correspondingpublic encryption key
![image](https://user-images.githubusercontent.com/49055941/146977483-910b244f-ab0b-4968-abac-7fbf14c37be5.png)
