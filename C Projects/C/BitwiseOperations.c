/* 
 * CS:APP Data Lab 
 * 
 * Ben Schwartz
 * 
 * bits.c - Source file with your solutions to the Lab.
 *          This is the file you will hand in to your instructor.
 *
 * WARNING: Do not include the <stdio.h> header; it confuses the dlc
 * compiler. You can still use printf for debugging without including
 * <stdio.h>, although you might get a compiler warning. In general,
 * it's not good practice to ignore compiler warnings, but in this
 * case it's OK.  
 */

#if 0
/*
 * Instructions to Students:
 *
 * STEP 1: Read the following instructions carefully.
 */

You will provide your solution to the Data Lab by
editing the collection of functions in this source file.

INTEGER CODING RULES:
 
  Replace the "return" statement in each function with one
  or more lines of C code that implements the function. Your code 
  must conform to the following style:
 
  int Funct(arg1, arg2, ...) {
      /* brief description of how your implementation works */
      int var1 = Expr1;
      ...
      int varM = ExprM;

      varJ = ExprJ;
      ...
      varN = ExprN;
      return ExprR;
  }

  Each "Expr" is an expression using ONLY the following:
  1. Integer constants 0 through 255 (0xFF), inclusive. You are
      not allowed to use big constants such as 0xffffffff.
  2. Function arguments and local variables (no global variables).
  3. Unary integer operations ! ~
  4. Binary integer operations & ^ | + << >>
    
  Some of the problems restrict the set of allowed operators even further.
  Each "Expr" may consist of multiple operators. You are not restricted to
  one operator per line.

  You are expressly forbidden to:
  1. Use any control constructs such as if, do, while, for, switch, etc.
  2. Define or use any macros.
  3. Define any additional functions in this file.
  4. Call any functions.
  5. Use any other operations, such as &&, ||, -, or ?:
  6. Use any form of casting.
  7. Use any data type other than int.  This implies that you
     cannot use arrays, structs, or unions.

 
  You may assume that your machine:
  1. Uses 2s complement, 32-bit representations of integers.
  2. Performs right shifts arithmetically.
  3. Has unpredictable behavior when shifting an integer by more
     than the word size.

EXAMPLES OF ACCEPTABLE CODING STYLE:
  /*
   * pow2plus1 - returns 2^x + 1, where 0 <= x <= 31
   */
  int pow2plus1(int x) {
     /* exploit ability of shifts to compute powers of 2 */
     return (1 << x) + 1;
  }

  /*
   * pow2plus4 - returns 2^x + 4, where 0 <= x <= 31
   */
  int pow2plus4(int x) {
     /* exploit ability of shifts to compute powers of 2 */
     int result = (1 << x);
     result += 4;
     return result;
  }

FLOATING POINT CODING RULES

For the problems that require you to implent floating-point operations,
the coding rules are less strict.  You are allowed to use looping and
conditional control.  You are allowed to use both ints and unsigneds.
You can use arbitrary integer and unsigned constants.

You are expressly forbidden to:
  1. Define or use any macros.
  2. Define any additional functions in this file.
  3. Call any functions.
  4. Use any form of casting.
  5. Use any data type other than int or unsigned.  This means that you
     cannot use arrays, structs, or unions.
  6. Use any floating point data types, operations, or constants.


NOTES:
  1. Use the dlc (data lab checker) compiler (described in the handout) to 
     check the legality of your solutions.
  2. Each function has a maximum number of operators (! ~ & ^ | + << >>)
     that you are allowed to use for your implementation of the function. 
     The max operator count is checked by dlc. Note that '=' is not 
     counted; you may use as many of these as you want without penalty.
  3. Use the btest test harness to check your functions for correctness.
  4. Use the BDD checker to formally verify your functions
  5. The maximum number of ops for each function is given in the
     header comment for each function. If there are any inconsistencies 
     between the maximum ops in the writeup and in this file, consider
     this file the authoritative source.

/*
 * STEP 2: Modify the following functions according the coding rules.
 * 
 *   IMPORTANT. TO AVOID GRADING SURPRISES:
 *   1. Use the dlc compiler to check that your solutions conform
 *      to the coding rules.
 *   2. Use the BDD checker to formally verify that your solutions produce 
 *      the correct answers.
 */


#endif
/* Copyright (C) 1991-2016 Free Software Foundation, Inc.
   This file is part of the GNU C Library.

   The GNU C Library is free software; you can redistribute it and/or
   modify it under the terms of the GNU Lesser General Public
   License as published by the Free Software Foundation; either
   version 2.1 of the License, or (at your option) any later version.

   The GNU C Library is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public
   License along with the GNU C Library; if not, see
   <http://www.gnu.org/licenses/>.  */
/* This header is separate from features.h so that the compiler can
   include it implicitly at the start of every compilation.  It must
   not itself include <features.h> or any other header that includes
   <features.h> because the implicit include comes before any feature
   test macros that may be defined in a source file before it first
   explicitly includes a system header.  GCC knows the name of this
   header in order to preinclude it.  */
/* glibc's intent is to support the IEC 559 math functionality, real
   and complex.  If the GCC (4.9 and later) predefined macros
   specifying compiler intent are available, use them to determine
   whether the overall intent is to support these features; otherwise,
   presume an older compiler has intent to support these features and
   define these macros by default.  */
/* wchar_t uses Unicode 8.0.0.  Version 8.0 of the Unicode Standard is
   synchronized with ISO/IEC 10646:2014, plus Amendment 1 (published
   2015-05-15).  */
/* We do not support C11 <threads.h>.  */
/* 
 * evenBits - return word with all even-numbered bits set to 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 8
 *   Rating: 1
 */
int evenBits(void) {
  //continuously or word with 01010101 and then shift word 8 bits to the left
  int word = 0x55 << 8;
  word = word | 0x55;
  word = word << 8;
  word = word | 0x55;
  word = word << 8;
  word = word | 0x55;
  return word;
}
/* 
 * addOK - Determine if can compute x+y without overflow
 *   Example: addOK(0x80000000,0x80000000) = 0,
 *            addOK(0x80000000,0x70000000) = 1, 
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 20
 *   Rating: 3
 */
int addOK(int x, int y) {
  int add = x + y;
  int signX = x>>31;
  int signY = y>>31;
  int signAdd = add>>31;

  //If the sign bits of x and y are different then one is negative and
  //one is positive so there would not be overflow
  int check1 = !!(signX^signY);

  //If the sign of x and y are the same then the sign should be the same after adding
  //so if the sign of x matches the sign of add there was no overflow.
  int check2 = !(signX^signAdd);

  return check1 | (check2);
}
/* 
 * conditional - same as x ? y : z 
 *   Example: conditional(2,4,5) = 4
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 16
 *   Rating: 3
 */
int conditional(int x, int y, int z) {
  //0 for x=0 and 1 otherwise
  int boolX = !!x;

  //0 for x=0 and 11111... otherwise
  int mask = ~boolX + 1;

  //return z when x=0 and y otherwise
  return (mask&y) | (~mask&z);
}
/* 
 * absVal - absolute value of x
 *   Example: absVal(-1) = 1.
 *   You may assume -TMax <= x <= TMax
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 10
 *   Rating: 4
 */
int absVal(int x) {
  //gives all 1s if x is negative and all 0s if x is positive
  int mask = x>>31;

  //If x is positive: x^0 + (11111...+00...01) gives x+0 = x
  //If x is negaitive: x^(11111...) + (0000... + 000...01) = ~x+1 = -x = abs(x)
  return (x^mask) + (~mask+1);
}
/*
 * bitParity - returns 1 if x contains an odd number of 0's
 *   Examples: bitParity(5) = 0, bitParity(7) = 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 20
 *   Rating: 4
 */
int bitParity(int x) {
  /*
  xOR gives you the parity of the bits being compared.

  xOR the first two bits, then those bits with the second two and so on.
  This essentially recursively xORs every bit and each time the msb of
  the section will give us the parity of that section.
  This leads to the msb giving us the parity of the entire integer
  */
  x ^= x << 1;
  x ^= x << 2;
  x ^= x << 4;
  x ^= x << 8;
  x ^= x << 16;

  x &= 1<<31;

  return !!x;
}
/* 
 * fitsShort - return 1 if x can be represented as a 
 *   16-bit, two's complement integer.
 *   Examples: fitsShort(33000) = 0, fitsShort(-32768) = 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 8
 *   Rating: 1
 */
int fitsShort(int x) {
  /*
  If x can be represented as a 16-bit two's complement
  the last 16 bits must all be zero
  So shift x 16 to the left and then 16 to the right
  and check if it remained the same
  */
  int x1 = x<<16;
  int x2 = x1>>16;
  int isEqual = !(x^x2);

  return isEqual;
}
/* 
 * copyLSB - set all bits of result to least significant bit of x
 *   Example: copyLSB(5) = 0xFFFFFFFF, copyLSB(6) = 0x00000000
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 5
 *   Rating: 2
 */
int copyLSB(int x) {
  //move the lsb into the furthest left bit
  int lsb = x<<31;

  //lsb becomes 1 if it is 1000... and 0 if it is 000...
  lsb = !!lsb;

  //If lsb is 1 ~lsb becomes 111...110 so add 1 to get 1111...
  //If lsb is 0 ~lsb becomes 11111... so add 1 to get 000...
  return ~lsb+1;
}
/* 
 * oddBits - return word with all odd-numbered bits set to 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 8
 *   Rating: 2
 */
int oddBits(void) {
  //continuously or word with 10101010 and then shift it 8 bits to the left
  int word = 0xaa << 8;
  word = word | 0xaa;
  word = word << 8;
  word = word | 0xaa;
  word = word << 8;
  word = word | 0xaa;
  return word;
}
/* 
 * isGreater - if x > y  then return 1, else return 0 
 *   Example: isGreater(4,5) = 0, isGreater(5,4) = 1
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 24
 *   Rating: 3
 */
int isGreater(int x, int y) {
  //Checks if x-y is negative
  //fails when there is overflow
  int greaterEqual = !((x+ (~y+1))&1<<31);

  //Checks if x is equal to y
  int equal = !(x^y);

  //extra cases to deal with the overflow issue
  //If x is negative and y is positive we want to return 0
  //If y is negative and x is positive we want to return 1


  //check if x is negative
  int negX = ((x>>31)&1);

  //check if y is negative
  int negY = ((y>>31)&1);

  return (greaterEqual & ~equal & !(negX & !negY)) | ((!negX) & negY);
}
/* 
 * isAsciiDigit - return 1 if 0x30 <= x <= 0x39 (ASCII codes for characters '0' to '9')
 *   Example: isAsciiDigit(0x35) = 1.
 *            isAsciiDigit(0x3a) = 0.
 *            isAsciiDigit(0x05) = 0.
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 15
 *   Rating: 3
 */
int isAsciiDigit(int x) {
  //check if x>=0x30
  //If x-0x30 is positive the sign bit will be 0
  int greaterThan = !((x + (~0x30 + 1))& 1<<31);

  //check if x<=0x39
  //If 0x39-x is positive the sign bit will be 0
  int lessThan = !((0x39 + (~x+1)) & 1<<31);

  return greaterThan & lessThan;
}
/* 
 * leastBitPos - return a mask that marks the position of the
 *               least significant 1 bit. If x == 0, return 0
 *   Example: leastBitPos(96) = 0x20
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 6
 *   Rating: 2 
 */
int leastBitPos(int x) {
  /*
  ~x+1 leaves the least significant 1 and all the following 0s and
  flips the rest of the bits
  So x&(~x+1) gives all zeros except the least significant 1 stays
  which gives 2^k where k is the position of the remaining 1
  */
  int mask = x & (~x + 1);
  return mask;
}
/* 
 * greatestBitPos - return a mask that marks the position of the
 *               most significant 1 bit. If x == 0, return 0
 *   Example: greatestBitPos(96) = 0x40
 *   Legal ops: ! ~ & ^ | + << >>
 *   Max ops: 70
 *   Rating: 4 
 */
int greatestBitPos(int x) {

  //Make every bit right of the most significant 1 a 1
  x |= x >> 1;
  x |= x >> 2;
  x |= x >> 4;
  x |= x >> 8;
  x |= x >> 16;

  //If you shift x one to the right and xOR it to itself it
  //changes every bit right of the ms 1 to a 0
  //If the most signigicant 1 is the most significant bit of x
  //y will become 0, failing to mark the position correctly
  //int y = x ^ (x>>1);

  //If y becomes 0 we can make every bit of x 0 except the most significant 
  //bit and return that instead
  //int z = x & 1<<31;

  //y and z were causing parse errors with dlc so I am just going to return the 
  //expressions rather than the variables

  return (x^(x>>1)) | (x & 1<<31);

}
/* 
 * float_abs - Return bit-level equivalent of absolute value of f for
 *   floating point argument f.
 *   Both the argument and result are passed as unsigned int's, but
 *   they are to be interpreted as the bit-level representations of
 *   single-precision floating point values.
 *   When argument is NaN, return argument..
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 10
 *   Rating: 2
 */
unsigned float_abs(unsigned uf) {
  //change the sign bit to 0
  unsigned abs = uf&0x7FFFFFFF;


  //The argument is NaN if the exponent bits are all 1's
  if (abs >= 0x7F800001){
    return uf;
  }
  else{
    return abs;
  }
}
/* 
 * float_f2i - Return bit-level equivalent of expression (int) f
 *   for floating point argument f.
 *   Argument is passed as unsigned int, but
 *   it is to be interpreted as the bit-level representation of a
 *   single-precision floating point value.
 *   Anything out of range (including NaN and infinity) should return
 *   0x80000000u.
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 30
 *   Rating: 4
 */
int float_f2i(unsigned uf) {
  //Ha helped me a lot when she explained some of the ideas of this
  //and the following exercise during class on Friday.
  
  //Shift it according to the real exponent (exp - bias)

  unsigned sign = uf>>31;
  unsigned exp = (uf>>23) & 0xFF;
  unsigned E = exp - 0x7F;
  unsigned frac = (uf & 0x7FFFFF);

  //case for NaN and inf
  if (exp == 0xFF){
    return 0x80000000u;//inf
  }
  
  //denormalized case
  if (exp < 0x7F){
    return 0x0;
  }

  //NaN or inf
  if(E >= 31){
    return 0x80000000u;
  }

  //Shift the fraction according to the exponent
  if(E > 22){
    frac = frac << (E - 23);
  }
  else{
    frac = frac >> (23 - E);
  }

  //The fraction refers to 1.[frac] so we need to add a 1 to the beginning of frac
  frac += 1<<E;

  //If the sign bit is 1 the returned value is negative
  if(sign == 1){
    frac = -frac;
  }

  return frac;
}
/* 
 * float_half - Return bit-level equivalent of expression 0.5*f for
 *   floating point argument f.
 *   Both the argument and result are passed as unsigned int's, but
 *   they are to be interpreted as the bit-level representation of
 *   single-precision floating point values.
 *   When argument is NaN, return argument
 *   Legal ops: Any integer/unsigned operations incl. ||, &&. also if, while
 *   Max ops: 30
 *   Rating: 4
 */
unsigned float_half(unsigned uf) {
  /*
  check if the number is inf or NaN
  check if the exponent is 0 -> shift the fraction to the right one;
  else subtract 1 from exp
  sign | frac to get the correct sign
  */
  unsigned sign = uf & 0x80000000;
  unsigned exp = uf & 0x7f800000;
  unsigned frac = uf & 0x7FFFFFF;

  //If the last two bits are both 1 add 1 for rounding
  frac += ((uf & 3) >> 1)& (uf & 1);

  if (exp == 0x7f800000){
    return uf;
  }
  else if(exp <= 0x00800000){
    return sign | (frac >> 1);
  }
  else{
    return uf - 0x00800000;
  }
}
