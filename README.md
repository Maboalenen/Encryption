RSA_Encryption
==========

RSA
-----

> First published by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977, RSA implements a public-key cryptosystem, as well as digital signatures

 * Public-key encryption     
> In RSA, encryption keys are public, while the decryption keys are not, so only the person with the correct decryption key can decipher an encrypted message.

* Digital signatures                          

> The receiver may need to verify that a transmitted message actually originated from the sender (signature)This is done using the sender’s decryption key, and the signature can later be verified by anyone, using the corresponding public encryption key

RSA operation
-----
RSA algorithm involves four step    
1- Key-generation. (e,d).   
2- key distribution.    
3- Encryption     
4- Decryption   

Generate-keys 
-----
> Key length greater than 1024.   
> RSA Cipher there are two key pairs
> Each user has their own encryption and decryption procedures, e,n and d,n ,    
     <br/>- E Public exponent  
    - D Secret exponent  
 - N is the module number  

Five mythical step to generate Keys 
-----
              
  1-  two prime number p,q                      
  <br />- p and q length greater than 512               
      
  2-  N=multiplication of the two prime number (p,q)                      
  <br /> - N = (p)(q)                  
         - N using during the encryption and decryption.                   
      
  3-  Euler’s Totient Function 
      -  This function outputs the number of integers between (0) and (n) that are relatively prime to n                                                                           
      -  means  Φ(n)= (p-1)(q-1)                                                             
      
  4-  Choose e                                      
      - Must be less than Φ(n)                 
      - coprime with n,Φ(n)            
      
  5- Choose d  (e*d mod Φ(n) =1 )                         
  
  Result
  ----
  public key = e,n    
  private key = d,n 
