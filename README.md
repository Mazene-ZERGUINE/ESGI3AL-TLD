# Projet mini langage

## Affectation
```js
x = 4; 
x = x + 5;

print(x); 
// 7
```

## Instructions conditionnelles
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