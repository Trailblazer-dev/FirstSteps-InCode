#include <stdio.h>

int main() {
    int sales[4][3] = {
        {210, 315, 205},
        {310, 290, 125},
        {315, 135, 240},
        {360, 410, 480}
    };

    // Calculate the total value of each sale
    int totals[4] = {0, 0, 0, 0};
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 3; j++) {
            totals[i] += sales[i][j];
        }
    }

    // Print the total value of each sale for each sales team
    printf("Sales A total: %d\n", totals[0]);
    printf("Sales B total: %d\n", totals[1]);
    printf("Sales C total: %d\n", totals[2]);
    printf("Sales D total: %d\n", totals[3]);

    // Calculate the total sales for each item
    int item_totals[3] = {0, 0, 0};
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 4; j++) {
            item_totals[i] += sales[j][i];
        }
    }

    // Print the total sales for each item
    printf("\nTotal sales for item1: %d\n", item_totals[0]);
    printf("Total sales for item2: %d\n", item_totals[1]);
    printf("Total sales for item3: %d\n", item_totals[2]);

    // Calculate the grand total sales for all items
    int grand_total = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 3; j++) {
            grand_total += sales[i][j];
        }
    }

    // Print the grand total sales for all items
    printf("\nGrand total sales for all items: %d\n", grand_total);

    return 0;
}
