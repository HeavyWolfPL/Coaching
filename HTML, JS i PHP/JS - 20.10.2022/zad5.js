function policz(a, b){
    let liczby = 0;
    let tablica = []
    for(let i=a; i<=b; i++){
        tablica.push(i)
    }
    console.log(tablica)
    return tablica;
}

function suma(){
    let suma = 0;
    console.log(arguments)
    // arguments =        0            1    2
    // arguments = [[funkcja policz], ..., ...]
    let tablica = arguments[0]; // arguments[0] = [funkcja policz]
    for(let i = tablica[0]; i <= tablica.length; i++){
        suma += i
    }
    return suma;
}
//   0  1  2  3  4
suma(1, 2, 3, 4, 5)

console.log(suma(policz(1,5)))

// suma(policz(1,5))
//      =
// suma(arguments)



