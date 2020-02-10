# Baby Language 👶

Can you figure out what are babies speaking?

## Demo

You got the message from a baby!

```
googoogoogoo goo googagoogoo googagoogoo gagaga gagoogagoogaga
googoo googagagagagoo gaga coo googoogoogoo googooga gagoo gagagoo googagoo gagoogaga gagoogagoogaga
```

What is he/she says!?

Calm down. Let's figure out what he/she says.

```
$ python baby.py 
input mode (d: decode, e: encode) > d
input your message > googoogoogoo goo googagoogoo googagoogoo gagaga gagoogagoogaga
HELLO!
input your message > googoo googagagagagoo gaga coo googoogoogoo googooga gagoo gagagoo googagoo gagoogaga gagoogagoogaga
I'M HUNGRY!
```

OK! We got it! Hooray🙌  
If you want to speak baby language, you can translate like this.

```
$ python baby.py 
input mode (d: decode, e: encode) > e
input your message > I'm a baby!
googoo googagagagagoo gaga coo googa coo gagoogoogoo googa gagoogoogoo gagoogaga gagoogagoogaga
```

## Customize

You can also customize baby words, by editing `baby.yml` and `baby.py > class Baby() > lang_type`.  
Let's see Japanese baby version.

```
(edit baby.py > Baby() > lang_type = 'Japanese')
$ python baby.py 
input mode (d: decode, e: encode) > e
input your message > Hello!
ババババ バ バブーババ バブーババ ブーブーブー ブーバブーバブーブー
```

Japanese baby speaks like "バブー"!

## Usage

Only execute `baby.py` on python3.

```
$ python baby.py
```

If you want run tests, execute shell script as follow.

```
$ cd baby-language
$ ./exec_test.sh
```

## Limitation

* If there are some invalid input characters, the output becomes like `googaga*invalid_char*ga googagoo`.