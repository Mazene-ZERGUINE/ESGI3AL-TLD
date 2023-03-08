# Projet mini langage

## Affectation
```js
x = 4; 
x = x + 5;

print(x); 
// CALC >>  9
```

## multi comparaison 
```
js 
x = 1 < 2 OR 2 > 1 ; 
print(x) ; 

/* CALC >> True */ 
```

## multi print 
,,,
js 

x = 3 ; 
y = 2 ;

print(x , y , 12) ;
/* 
CALC >> 3 
CALC >> 2 
CALC >> 12
 */


 print("hello world" , 2 , "toto") ;
 /*  
 CALC >> hello world
 CALC >> 2 
 CALC >> toto
 */
,,,

## global static variables
````
python
def x = 2 ; 
x = 5 ; 
print(x) ;

/* CALC >>  2 */
```

## Instructions conditionnelles
```js

x = 3 ; 
if (x == 3) -> print(x) ;
// CALC >>  3
```

```js
x = 2;

if (x == 2) -> {
    n = 2; 
    print(n);

    if (x == 2) -> {
        n = 22;
        print(n);
    }
}

// CALC >>  2
// CALC >>  22
```

```js
x = 1;

if (x == 4) -> {
    print(x); 
} elseif (x < 4) -> {
    print "x < 4";
} else {
    print "x > 4"; 
}

// CALC >>  x < 4
```

## While, for imbriques
`for` :
```js
for (i = 1 to 3 , i++) {
    print "i";

    for (j = 1 to 3 , j++) {
      print "J";
    }
}
// CALC >>  i
// CALC >>  J
// CALC >>  J
// CALC >>  J
// CALC >>  i
// CALC >>  J
// CALC >>  J
// CALC >>  J
// CALC >>  i
// CALC >>  J
// CALC >>  J
// CALC >>  J
```

`while` :
```js
i = 0;
j = 0;

while( i < 3 ) {
    print(i);
    i++;

    while( j < 3 ) {
      print(j);
      j++;
    }
}
// CALC >>  0
// CALC >>  0
// CALC >>  1
// CALC >>  2
// CALC >>  1
// CALC >>  2
```

## Affichage de valeur et de chaine de caracteres
```js
print(2 * 5);
// CALC >>  10
```

```python
print "Bonjour Toto";
# CALC >>  Bonjour Toto
```

## Fonction sans parametre
Appel de fonction avec une boucle :
```kotlin
fun test() 
    start 
        print "Bonjour Toto";
    end 

test();
// CALC >>  Bonjour Toto
```

## Fonction avec parametre
```kotlin
fun multiParams(a , b , c)
    start
        print(a + b);
        print(c);
    end

multiParams(1, 4, 8);
// CALC >>  5
// CALC >>  8
```

## Fonction avec parametre et return
```kotlin
fun demo(a)
    start
        if (a == 1) -> return a ;
        return a +5 ;
    end

demo(2);
// CALC >> ret value : 7
```