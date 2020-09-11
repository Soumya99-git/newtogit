function fibonacci(x) {
    if (x <= 1) {
        return x
    }
    else {
        return fibonacci(x - 1) + fibonacci(x - 2);
    }
}
let sum = 0
for (let i = 0; i < 5; i = i + 1) {
    sum = sum + fibonacci(i)
    console.log(fibonacci(i))
}

console.log(sum)

var x = prompt("Enter the Switch value")
x = parseInt(x)
switch (x) {
    case 0:
        console.log(0)
        break;
    case 1:
        console.log(1)
        break;
    case 2:
        console.log(2)
        break;
    case 3:
        console.log(3)
        break;
    default:
        console.log("Fu** you")
        break;

}