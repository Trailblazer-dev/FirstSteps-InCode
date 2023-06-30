#include <stdio.h>
#include <string.h>

int main() {
    char number[12];
    printf("Enter your mobile number please\n");
    fgets(number, sizeof(number), stdin);
    while (strlen(number) != 11 || number[strcspn(number, "\n")] != '\0') {
        printf("Please enter your phone number in the right format\n");
        fgets(number, sizeof(number), stdin);
        number[strcspn(number, "\n")] = '\0';
    }
    printf("successful thank-you");
    return 0;
}
/* strcspn() function is used to find the position of the newline character in the string,
 and the corresponding element in the array is replaced with a null terminator (\0). This 
ensures that the string has a length of 11 and does not contain any newline characters.

*/