# Projet mini langage

## Affectation
```js
x = 4; 
x = x + 5;

print(x); 
// 9
```

## Instructions conditionnelles
```js

x = 3 ; 
if (x == 3) -> print(x) ;
// 3 

x = 2;

if (x == 2) -> {
    n = 2; 
    print(n);

    if (x == 2) -> {
        n = 22;
        print(n);
    }
}

// 2
// 22
```

```js
if (x == 4) -> {
    print(x); 
} elseif (x < 4) -> {
    print "ok";
} else {
    print "x < 4"; 
}

// ok
```

## While, for imbriques

```js
    /* for loop */
    for (i = 0 to 3 , i++) {
        print "toto" ; 
    } 
    /* 
    toto 
    toto 
    toto
    */

   /*  while loop */
   i = 0 ;
   while( i < 3 ) {
    print (i) ;
   }
   /* 
   0
   1
   2
   */
```
...

## Affichage de valeur et de chaine de caracteres
```js
print(2 * 5);
// 10
```

```python
print "Bonjour Toto";
# Bonjour Toto
```

## Fonction sans parametre
Appel de fonction avec une boucle :
```kotlin
fun test() 
    start 
        print "Bonjour Toto";
    end 

test();
// Bonjour Toto
```

## Fonction avec parametre
```kotlin
fun multiParams (a , b , c)
    start
        print(a + b);
        print(c);
    end

multiParams(1, 4, 8);
// 5
// 8
```

## Fonction avec parametre et return
```kotlin
fun demo (a)
    start
        if (a == 1) -> return a ;
        return a +5 ;
    end

demo(2);
/* CALC >> ret value : 7  */
```