#include <iostream>
using namespace std;
/* PSEUDOCODE:
    int x, y
    while loop for numbers less than 4,000,000
    if sum1 of x + y is evem
        then y value is added to sum2
    y value is assigned to x
    sum1 value is assigned to y to proceed to the next summation in the sequence 
*/

int main(){
    int sum1, sum2, x, y;

    while (y <= 4000000){
        sum = x + y;
        if (sum1 % 2 == 0){
            sum2 += y;
        }
        x = y;
        y = sum1;
    }

    cout << sum2;

}