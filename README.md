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
if (x == 2) -> {
    n = 2; 
    print (n);

    if (x == 2) -> {
        n = 22;
        print (n);
    }
}
```

```js
if (False) {
    print(1);
} elif (True) {
    print(777);
} else {
    print(0);
};

// 777
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