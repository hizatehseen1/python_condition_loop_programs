print("==================================================")
print("     SMART PHARMACY INVENTORY & SALES SYSTEM      ")
print("==================================================")

# 1. Ask how many different medicines need to be processed
try:
    num_medicines = int(input("Enter the number of different medicines to process: "))
    
    if num_medicines <= 0:
        print("\nError: Number of medicines must be greater than zero.")
    else:
        # Initialize accumulators and counters for the final report
        total_revenue = 0.0
        restock_count = 0
        restock_medicines_list = []

        print("-" * 50)

        # 2. Use a for loop to process each medicine
        for i in range(1, num_medicines + 1):
            print(f"\n--- Processing Medicine {i} of {num_medicines} ---")
            
            # 3. Collect medicine details
            med_name = input("Enter medicine name: ").strip()
            if not med_name:
                print("Error: Medicine name cannot be empty. Skipping this entry.")
                continue

            try:
                stock = int(input("Enter available stock (units): "))
                price = float(input("Enter price per unit (Rs.): "))
                qty_sold = int(input("Enter quantity sold: "))

                # Validate non-negative numbers
                if stock < 0 or price < 0 or qty_sold < 0:
                    print("Error: Stock, price, and quantity cannot be negative. Skipping this entry.")
                    continue

            except ValueError:
                print("Error: Invalid numeric input. Please enter valid numbers. Skipping this entry.")
                continue

            # 4. Check whether requested sales quantity is available in stock
            if qty_sold > stock:
                print(f"❌ Error: Insufficient stock! Only {stock} units available, but {qty_sold} requested.")
                print(f"Status for {med_name}: Sale could not be processed.")
                
                # Even if the sale fails, check if existing stock is low (< 10)
                remaining_stock = stock
            else:
                # 5. Calculate total sales amount for successfully processed medicine
                sale_amount = qty_sold * price
                
                # 6. Calculate remaining stock after sale
                remaining_stock = stock - qty_sold
                
                # 8. Maintain total pharmacy revenue using an accumulator
                total_revenue += sale_amount

                print(f"\n[Sale Successful]")
                print(f"Item Total Sales : Rs. {sale_amount:,.2f}")
                print(f"Remaining Stock  : {remaining_stock} units")

            # 7. Display low-stock warning if remaining stock is below 10 units
            if remaining_stock < 10:
                print(f"⚠️ LOW STOCK WARNING: '{med_name}' has only {remaining_stock} units left!")
                # 9. Count how many medicines require restocking
                restock_count += 1
                restock_medicines_list.append(med_name)

        # 10. Generate the final summary report
        print("\n" + "=" * 50)
        print("          PHARMACY DAILY SALES & INVENTORY REPORT")
        print("=" * 50)
        print(f"Total Medicines Processed : {num_medicines}")
        print(f"Total Pharmacy Revenue    : Rs. {total_revenue:,.2f}")
        print(f"Medicines Requiring Restock: {restock_count}")
        
        if restock_count > 0:
            print("Items to Restock (< 10 units):")
            for med in restock_medicines_list:
                print(f"  • {med}")
        else:
            print("All medicine stocks are sufficient!")
            
        print("=" * 50)

except ValueError:
    print("\nError: Please enter a valid integer for the number of medicines.")
