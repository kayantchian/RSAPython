'''
Criado por Kayan Tchian
24/02/2019
Ainda não testei com valores astronomicos como 10^100, se der algum bug com eles
fique avontade para fazer seu request
'''
import sys
class RSA_Calculator():
   def __init__(self):
      self.ascii,self.RSA,self.RSAN = [],[],[]
      self.text,self.p,self.q,self.e,self.euler,self.d,self.n,self.C,self.tag, self.CN= None,None,None,None,None,None,\
                                                                                         None,None,None,None
       #MAIN
   def Main(self):
      self.tag = input('\n  Choose \n'
                          '[0] EXIT\n'
                          '[1] ENCODE\n'
                          '[2] DECODE\n'
                          '>> ')
      while self.tag not in ['0','1','2']:
         print('Method not found !')
         self.tag = input('  Choose \n'
                          '[0] EXIT\n'
                          '[1] ENCODE\n'
                          '[2] DECODE\n'
                          '>> ')
      if self.tag == '0':
         sys.exit()
      elif self.tag == '1':
         self.Ascii()
         self.Values()
         self.FunctionEuler()
         self.E_Value()
         self.D_Value()
         self.Keys()
         self.Encryptation()
         self.Main()
      elif self.tag == '2':
         self.RSANumbers()
         self.DEValues()
         self.Decryptation()
         self.AsciiToText()
         
           # ENCRYPTATION
   def Ascii(self):
      self.text = input('Text: ')
      self.ascii = [ord(c) for c in self.text]
      print('    ASCII TEXT    ')
      print(self.ascii)
      print()
      return 'There is modular inverse'
   def Values(self):
      self.p = int(input('P Value ( Prime Number ) :'))
      factors,factors2 = [],[]
      for x in range(1,self.p+1):
         if (self.p% x) == 0:
            factors.append(x)
            if len(factors) > 2:
               print('\nThe Value isn\'t Prime Number')
               self.p = int(input('P Value ( Prime Number ) :'))
            else:
               pass
      self.q = int(input('Q Value { Prime Number ) : '))
      for x in range(1,self.q+1):
         if (self.q% x) == 0:
            factors2.append(x)
            if len(factors2) > 2:
               print('\nThe Value isn\'t Prime Number')
               self.q = int(input('Q Value ( Prime Number ) :'))
            else:
               pass
      self.n = self.p * self.q
      print(f'\nMod n is {self.n}')
   def FunctionEuler(self):
      self.euler = (self.p-1) * (self.q-1)
      print(f'\nFunction Euler is.. n = {self.euler}\n')
   def E_Value(self):
      factors = []
      self.e = int(input('(range 1 from n and prime number)\nE value:  '))
      if self.e not in range(1,self.e+1):
         print('E Value ins\'t in range(1 from n) ')
         self.e = int(input('(range 1 from n and prime number)\nE value:  '))
      else:
         pass
      for x in range(1,self.e+1):
         if (self.e% x) == 0:
            factors.append(x)
            if len(factors) > 2:
               print('\nThe Value isn\'t Prime Number')
               self.e = int(input('It isn\'t a prime number)\nE value:  '))
            else:
               pass
   '''def inverseMod(self):
      for i in range(1,self.n):
         if ( self.e * i ) % self.n == 1:
            return i'''
   def D_Value(self):
      print(f'\nD Value ( d * e ≡ 1 mod {self.euler}')
      for i in range(1, self.euler):
         if (self.e * i) % self.euler == 1:
            self.d = i
      print(f'D Value is {self.d}')
   def Keys(self):
      print(f'\nPublic Keys : n = {self.n} , e = {self.e}')
      print(f'Private Keys : p = {self.p} , q = {self.q} , d = {self.d}\n')
   def Encryptation(self):
      for i in self.ascii:
         self.RSA.append(pow(i,self.e,self.n))
      print('   ENCRYPTED TEXT    ')
      print(self.RSA)
      print()
           #DECRYPTATION
   def RSANumbers(self):
      self.CN = input('ENCRYPTED TEXT: ')
      for string in self.CN.split(' '):
         self.RSAN.append(string)
      print()
      print('   RSA ENCRYPTED TEXT: ')
      print(self.RSAN)
      print()
   def DEValues(self):
      self.d = int(input('D Value: '))
      self.n = int(input('Mod n Value: '))
   def Decryptation(self):
      for char in self.RSAN:
         x = int(char)
         self.ascii.append(pow(x,self.d,self.n))
      print()
      print(' RSA >> ASCII')
      print(self.ascii)
      print()
   def AsciiToText(self):
      self.text = ''.join(chr(i) for i in self.ascii)
      print('   ASCII > TEXT   ')
      print(self.text)
      print()
RSA = RSA_Calculator()
RSA.Main()
