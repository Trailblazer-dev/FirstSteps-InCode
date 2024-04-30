#include <stdio.h>
#include <string.h>

int main() {
    char pass[20];
    char saved_pass[20];

    printf("Enter your password: ");
    fgets(pass, sizeof(pass), stdin);
    pass[strcspn(pass, "\n")] = '\0'; // Remove the newline character

    FILE *ptr;
    ptr = fopen("password.txt", "r");
    if (ptr == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    fscanf(ptr, "%s", saved_pass);
    fclose(ptr);

    int l = strcmp(pass, saved_pass);
    if (l == 0) {
        printf("Login successful\n");
    } else {
        printf("Login failed\n");
        return 1; // Exit the program if login fails
    }

    return 0;
}
