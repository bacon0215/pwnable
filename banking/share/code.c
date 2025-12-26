#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>

typedef struct {
    char account_holder[50];
    int balance;
} BankAccount;

void setup()
{
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stderr, 0, 2, 0);
}

void check_balance(BankAccount *account) {
    printf("Account holder: %s, Balance: %d\n", account->account_holder, account->balance);
}

void deposit(BankAccount *account, int amount) {
    if (amount <= 0) {
        printf("Deposit amount must be positive.\n");
        return;
    }
    account->balance += amount;
    printf("Deposited %d. New balance: %d\n", amount, account->balance);
}

void withdraw(BankAccount *account, int amount) {
    if (amount > account->balance) {
        printf("Insufficient funds.\n");
        return;
    }
    account->balance -= amount;
    printf("Withdrew %d. New balance: %d\n", amount, account->balance);
}

void buy_flag(BankAccount *acoount) {
    if(acoount->balance > 13371337) {
        int fd = open("/home/banking/flag", O_RDONLY);
        char buf[49] = {0, };
        read(fd, buf, sizeof(buf) - 1);
        write(1, buf, sizeof(buf) - 1);
        exit(0);
    }
    else { 
        printf("You don't have enough money.\n");
    }
}

int main() {
    setup();
    
    BankAccount account;
    
    // Initialize account
    printf("Enter account holder's name: ");
    fgets(account.account_holder, sizeof(account.account_holder), stdin);
    account.account_holder[strcspn(account.account_holder, "\n")] = 0; // Remove newline
    account.balance = 100000; // Initial balance

    int choice;
    int amount;

    while (1) {
        printf("\nBanking System:\n");
        printf("1. Check Balance\n");
        printf("2. Deposit\n");
        printf("3. Withdraw\n");
        printf("4. Exit\n");
        printf("5. Buy Flag\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                check_balance(&account);
                break;
            case 2:
                printf("Enter amount to deposit: ");
                scanf("%d", &amount);
                deposit(&account, amount);
                break;
            case 3:
                printf("Enter amount to withdraw: ");
                scanf("%d", &amount);
                withdraw(&account, amount);
                break;
            case 4:
                printf("Exiting...\n");
                exit(0);
            case 5:
                buy_flag(&account);
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }

    return 0;
}