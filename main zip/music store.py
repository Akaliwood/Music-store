import sqlite3
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import io
import xml.etree.ElementTree as ET
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def login_screen():

    login_window = tk.Tk()
    login_window.title("Login")
    login_window.state("zoomed")
    original_image = Image.open("images/guitarvai.jpg")

    resized_image = original_image.resize((800, 600))
    bg_photo = ImageTk.PhotoImage(resized_image)

    background_label = tk.Label(login_window, image=bg_photo)
    background_label.image = bg_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title = tk.Label(
        login_window,
        text="Music Store Login",
        font=("Arial", 24, "bold"),
        bg="#3E2723",
        fg="white"
    )
    title.pack(pady=20)



    def resize_background(event):
        if event.widget == login_window:
            resized_image = original_image.resize((event.width, event.height))
            bg_photo = ImageTk.PhotoImage(resized_image)

            background_label.config(image=bg_photo)
            background_label.image = bg_photo

    login_window.bind("<Configure>", resize_background)

    def check_login():
        username = username_entry.get()
        password = password_entry.get()

        password_hash = hash_password(password)

        conn = sqlite3.connect("music store.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM Employees
            WHERE Username = ?
            AND PasswordHash = ?
        """, (username, password_hash))

        user = cursor.fetchone()

        conn.close()

        if user:
            messagebox.showinfo("Success", "Login successful")
            login_window.destroy()
            open_main_window()
        else:
            messagebox.showerror("Error", "Invalid username or password")


    # USERNAME LABEL
    username_label = tk.Label(
        login_window,
        text="Username",
        bg="#3E2723",
        fg="white",
        font=("Arial", 13, "bold"),
        padx=10,
        pady=5
    )
    username_label.pack(pady=(20, 5))

    # USERNAME ENTRY
    username_entry = tk.Entry(
        login_window,
        font=("Arial", 14),
        bd=3,
        relief="flat",
        bg="#ECECEC",
        fg="black",
        justify="center",
        width=25
    )
    username_entry.pack(ipady=6)

    # PASSWORD LABEL
    password_label = tk.Label(
        login_window,
        text="Password",
        bg="#3E2723",
        fg="white",
        font=("Arial", 13, "bold"),
        padx=10,
        pady=5
    )
    password_label.pack(pady=(20, 5))

    # PASSWORD ENTRY
    password_entry = tk.Entry(
        login_window,
        show="*",
        font=("Arial", 14),
        bd=3,
        relief="flat",
        bg="#ECECEC",
        fg="black",
        justify="center",
        width=25
    )
    password_entry.pack(ipady=6)
    password_entry.bind("<Return>", lambda event: check_login())

    # LOGIN BUTTON
    login_button = tk.Button(
        login_window,
        text="LOGIN",
        command=check_login,
        bg="#8B5A2B",
        fg="white",
        activebackground="#A0522D",
        activeforeground="white",
        font=("Arial", 14, "bold"),
        relief="raised",
        bd=4,
        padx=20,
        pady=8,
        cursor="hand2"
    )
    login_button.pack(pady=30)

    login_window.mainloop()

def open_product_window():
    window.withdraw()
    selected_image_path = tk.StringVar()
    product_window = tk.Toplevel()
    product_window.title("Product Management")
    product_window.state("zoomed")

    # BACKGROUND IMAGE
    product_original_image = Image.open("images/Guitar3.jpg")

    product_resized_image = product_original_image.resize((800, 600))
    product_bg_photo = ImageTk.PhotoImage(product_resized_image)

    product_background_label = tk.Label(product_window, image=product_bg_photo)
    product_background_label.image = product_bg_photo
    product_background_label.place(x=0, y=0, relwidth=1, relheight=1)


    def resize_product_background(event):
        if event.widget == product_window:
            resized_image = product_original_image.resize((event.width, event.height))

            bg_photo = ImageTk.PhotoImage(resized_image)

            product_background_label.config(image=bg_photo)
            product_background_label.image = bg_photo

    product_window.bind("<Configure>", resize_product_background)

    # TITLE
    product_title_label = tk.Label(
        product_window,
        text="Product Management",
        font=("Arial", 18, "bold"),
        bg="#3E2723",
        fg="white"
    )
    product_title_label.pack(pady=10)

    # PRODUCT NAME
    product_name_label = tk.Label(
        product_window,
        text="Product Name",
        bg="#BCAAA4",
        fg="black",
        font=("Arial", 10, "bold")
    )
    product_name_label.pack()

    product_name_entry = tk.Entry(product_window)
    product_name_entry.pack()

    # CATEGORY
    category_label = tk.Label(
        product_window,
        text="Category",
        bg="#BCAAA4",
        fg="black",
        font=("Arial", 10, "bold")
    )
    category_label.pack()

    category_entry = tk.Entry(product_window)
    category_entry.pack()

    # PRICE
    price_label = tk.Label(
        product_window,
        text="Price",
        bg="#BCAAA4",
        fg="black",
        font=("Arial", 10, "bold")
    )
    price_label.pack()

    price_entry = tk.Entry(product_window)
    price_entry.pack()

    # STOCK
    stock_label = tk.Label(
        product_window,
        text="Stock Quantity",
        bg="#BCAAA4",
        fg="black",
        font=("Arial", 10, "bold")
    )
    stock_label.pack()

    stock_entry = tk.Entry(product_window)
    stock_entry.pack()

    image_preview_label = tk.Label(
        product_window,
        text="No image selected",
        bg="#BCAAA4",
        fg="black",
        font=("Arial", 10, "bold")
    )
    image_preview_label.pack(pady=5)
    search_label = tk.Label(
        product_window,
        text="Search Product",
        bg="#BCAAA4",
        fg="black",
        font=("Arial", 10, "bold")
    )
    search_label.pack()

    search_entry = tk.Entry(product_window)
    search_entry.pack()

    # TABLE
    product_table = ttk.Treeview(
        product_window,
        columns=("ID", "Name", "Category", "Price", "Stock"),
        show="headings"
    )
    product_table.configure(height=8)
    product_table["style"] = "Custom.Treeview"

    product_table.heading("ID", text="ID")
    product_table.heading("Name", text="Product Name")
    product_table.heading("Category", text="Category")
    product_table.heading("Price", text="Price")
    product_table.heading("Stock", text="Stock")

    product_table.column("ID", width=80, anchor="center")
    product_table.column("Name", width=250, anchor="center")
    product_table.column("Category", width=180, anchor="center")
    product_table.column("Price", width=120, anchor="center")
    product_table.column("Stock", width=120, anchor="center")

    product_table.tag_configure(
        "evenrow",
        background="#5C4033",
        foreground="white"
    )

    product_table.tag_configure(
        "oddrow",
        background="#7A4A24",
        foreground="white"
    )
    # CLEAR FIELDS
    def clear_product_fields():
        product_name_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        stock_entry.delete(0, tk.END)


    def choose_product_image():
        file_path = filedialog.askopenfilename(
            parent=product_window,
            title="Select Product Image",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png"),
                ("All files", "*.*")
            ]
        )

        if file_path:
            selected_image_path.set(file_path)
            messagebox.showinfo("Image Selected", "Product image selected", parent=product_window)

    def search_products():

        product_table.pack(pady=20)

        search_text = search_entry.get()

        conn = sqlite3.connect("music store.db")
        cursor = conn.cursor()

        cursor.execute("""
              SELECT ProductID, ProductName, Category, Price, StockQuantity
              FROM Products
              WHERE ProductName LIKE ?
                 OR Category LIKE ?
          """, (
            f"%{search_text}%",
            f"%{search_text}%"
        ))

        rows = cursor.fetchall()

        product_table.delete(*product_table.get_children())

        for index, row in enumerate(rows):

            if index % 2 == 0:
                product_table.insert(
                    "",
                    tk.END,
                    values=row,
                    tags=("evenrow",)
                )

            else:
                product_table.insert(
                    "",
                    tk.END,
                    values=row,
                    tags=("oddrow",)
                )

        conn.close()
    def view_products():

        product_table.pack(pady=20)

        conn = sqlite3.connect("music store.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT ProductID, ProductName, Category, Price, StockQuantity
            FROM Products
        """)

        rows = cursor.fetchall()

        product_table.delete(*product_table.get_children())

        for index, row in enumerate(rows):

            if index % 2 == 0:
                product_table.insert(
                    "",
                    tk.END,
                    values=row,
                    tags=("evenrow",)
                )

            else:
                product_table.insert(
                    "",
                    tk.END,
                    values=row,
                    tags=("oddrow",)
                )

        conn.close()

    # ADD PRODUCT
    def add_product():

        product_name = product_name_entry.get()
        category = category_entry.get()
        price = price_entry.get()
        stock = stock_entry.get()

        if product_name == "":
            messagebox.showerror("Error", "Product name required", parent=product_window)
            return

        if price == "" or stock == "":
            messagebox.showerror("Error", "Price and stock required", parent=product_window)
            return

        conn = sqlite3.connect("music store.db")
        cursor = conn.cursor()

        image_data = None

        if selected_image_path.get() != "":
            with open(selected_image_path.get(), "rb") as file:
                image_data = file.read()

        cursor.execute("""
            INSERT INTO Products
            (ProductName, Category, Price, StockQuantity, Image)
            VALUES (?, ?, ?, ?, ?)
        """, (product_name, category, price, stock, image_data))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Product added")

        clear_product_fields()
        view_products()

    # SELECT PRODUCT
    def select_product(event):

        selected = product_table.focus()
        values = product_table.item(selected, "values")

        if values:
            product_id = values[0]

            product_name_entry.delete(0, tk.END)
            product_name_entry.insert(0, values[1])

            category_entry.delete(0, tk.END)
            category_entry.insert(0, values[2])

            price_entry.delete(0, tk.END)
            price_entry.insert(0, values[3])

            stock_entry.delete(0, tk.END)
            stock_entry.insert(0, values[4])

            conn = sqlite3.connect("music store.db")
            cursor = conn.cursor()

            cursor.execute("""
                SELECT Image
                FROM Products
                WHERE ProductID = ?
            """, (product_id,))

            result = cursor.fetchone()
            conn.close()

            if result and result[0]:
                image_data = result[0]

                image = Image.open(io.BytesIO(image_data))
                image = image.resize((150, 120))

                photo = ImageTk.PhotoImage(image)

                image_preview_label.config(image=photo, text="")
                image_preview_label.image = photo
            else:
                image_preview_label.config(
                    image="",
                    text="No image stored"
                )
    # UPDATE PRODUCT
    def update_product():

        selected = product_table.focus()

        values = product_table.item(selected, "values")

        if not values:
            messagebox.showerror("Error", "Please select a product", parent=product_window)
            return

        product_id = values[0]

        product_name = product_name_entry.get()
        category = category_entry.get()
        price = price_entry.get()
        stock = stock_entry.get()

        conn = sqlite3.connect("music store.db")
        cursor = conn.cursor()
        image_data = None

        if selected_image_path.get() != "":
            with open(selected_image_path.get(), "rb") as file:
                image_data = file.read()

        cursor.execute("""
            UPDATE Products
            SET ProductName = ?,
                Category = ?,
                Price = ?,
                StockQuantity = ?,
                Image = ?
            WHERE ProductID = ?
        """, (
            product_name,
            category,
            price,
            stock,
            image_data,
            product_id
        ))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Product updated")

        clear_product_fields()
        view_products()

    # DELETE PRODUCT
    def delete_product():

        selected = product_table.focus()

        values = product_table.item(selected, "values")

        if not values:
            messagebox.showerror("Error", "Please select a product", parent=product_window)
            return

        product_id = values[0]

        conn = sqlite3.connect("music store.db")
        cursor = conn.cursor()

        cursor.execute("""
            DELETE FROM Products
            WHERE ProductID = ?
        """, (product_id,))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Product deleted")

        clear_product_fields()
        view_products()

    # BIND
    product_table.bind("<ButtonRelease-1>", select_product)

    # BUTTONS
    add_product_button = tk.Button(
        product_window,
        text="Add Product",
        command=add_product,
        **button_style
    )
    add_product_button.pack(pady=10)

    view_product_button = tk.Button(
        product_window,
        text="View Products",
        command=view_products,
        **button_style
    )
    view_product_button.pack(pady=5)


    update_product_button = tk.Button(
        product_window,
        text="Update Product",
        command=update_product,
        **button_style
    )
    update_product_button.pack(pady=5)

    delete_product_button = tk.Button(
        product_window,
        text="Delete Product",
        command=delete_product,
        **button_style
    )
    delete_product_button.pack(pady=5)
    image_button = tk.Button(
        product_window,
        text="Choose Image",
        command=choose_product_image,
        **button_style
    )
    image_button.pack(pady=5)

    search_product_button = tk.Button(
        product_window,
        text="Search Product",
        command=search_products,
        **button_style
    )
    search_product_button.pack(pady=5)

    def on_close():
        product_window.destroy()
        window.deiconify()
        window.state("zoomed")

    product_window.protocol("WM_DELETE_WINDOW", on_close)

def open_order_window():
    window.withdraw()
    order_window = tk.Toplevel()
    order_window.title("Order Management")
    order_window.state("zoomed")
    # ORDER WINDOW BACKGROUND IMAGE
    order_original_image = Image.open("images/Guitar4.jpg")

    order_resized_image = order_original_image.resize((800, 600))
    order_bg_photo = ImageTk.PhotoImage(order_resized_image)

    order_background_label = tk.Label(order_window, image=order_bg_photo)
    order_background_label.image = order_bg_photo
    order_background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def resize_order_background(event):
        if event.widget == order_window:
            resized_image = order_original_image.resize((event.width, event.height))
            bg_photo = ImageTk.PhotoImage(resized_image)

            order_background_label.config(image=bg_photo)
            order_background_label.image = bg_photo

    order_window.bind("<Configure>", resize_order_background)

    title = tk.Label(
        order_window,
        text="Order Management",
        font=("Arial", 18, "bold"),
        bg="#3E2723",
        fg="white"
    )
    title.pack(pady=10)

    customer_label = tk.Label(order_window, text="Customer", bg="#BCAAA4", fg="black", font=("Arial", 10, "bold"))
    customer_label.pack()

    customer_combo = ttk.Combobox(order_window, width=40)
    customer_combo.pack()

    product_label = tk.Label(order_window, text="Product", bg="#BCAAA4", fg="black", font=("Arial", 10, "bold"))
    product_label.pack()

    product_combo = ttk.Combobox(order_window, width=40)
    product_combo.pack()

    quantity_label = tk.Label(order_window, text="Quantity", bg="#BCAAA4", fg="black", font=("Arial", 10, "bold"))
    quantity_label.pack()

    quantity_entry = tk.Entry(order_window)
    quantity_entry.pack()

    def load_data():
        conn = sqlite3.connect("music store.db")
        cursor = conn.cursor()

        cursor.execute("SELECT CustomerID, FirstName, LastName FROM Customers")
        customers = cursor.fetchall()

        cursor.execute("SELECT ProductID, ProductName, Price FROM Products")
        products = cursor.fetchall()

        conn.close()

        customer_combo["values"] = [
            f"{c[0]} - {c[1]} {c[2]}" for c in customers
        ]

        product_combo["values"] = [
            f"{p[0]} - {p[1]} - £{p[2]}" for p in products
        ]

    order_table = ttk.Treeview(
        order_window,
        columns=("OrderID", "Customer", "Product", "Quantity", "Subtotal", "Date"),
        show="headings"
    )

    order_table["style"] = "Custom.Treeview"
    order_table.configure(height=8)

    order_table.heading("OrderID", text="Order ID")
    order_table.heading("Customer", text="Customer")
    order_table.heading("Product", text="Product")
    order_table.heading("Quantity", text="Quantity")
    order_table.heading("Subtotal", text="Subtotal")
    order_table.heading("Date", text="Date")
    def view_orders():

            order_table.pack(pady=20)

            conn = sqlite3.connect("music store.db")
            cursor = conn.cursor()

            cursor.execute("""
                SELECT 
                    Orders.OrderID,
                    Customers.FirstName || ' ' || Customers.LastName,
                    Products.ProductName,
                    OrderDetails.Quantity,
                    OrderDetails.Subtotal,
                    Orders.OrderDate
                FROM Orders
                JOIN Customers ON Orders.CustomerID = Customers.CustomerID
                JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
                JOIN Products ON OrderDetails.ProductID = Products.ProductID
            """)

            rows = cursor.fetchall()

            order_table.delete(*order_table.get_children())

            for row in rows:
                order_table.insert("", tk.END, values=row)

            conn.close()
    def export_orders_xml():
        conn = sqlite3.connect("music store.db")
        cursor = conn.cursor()

        cursor.execute("""
                SELECT 
                    Orders.OrderID,
                    Customers.FirstName || ' ' || Customers.LastName,
                    Products.ProductName,
                    OrderDetails.Quantity,
                    OrderDetails.Subtotal,
                    Orders.OrderDate
                FROM Orders
                JOIN Customers ON Orders.CustomerID = Customers.CustomerID
                JOIN OrderDetails ON Orders.OrderID = OrderDetails.OrderID
                JOIN Products ON OrderDetails.ProductID = Products.ProductID
            """)

        rows = cursor.fetchall()
        conn.close()

        root = ET.Element("Orders")
        for row in rows:
            order = ET.SubElement(root, "Order")

            ET.SubElement(order, "OrderID").text = str(row[0])
            ET.SubElement(order, "Customer").text = row[1]
            ET.SubElement(order, "Product").text = row[2]
            ET.SubElement(order, "Quantity").text = str(row[3])
            ET.SubElement(order, "Subtotal").text = str(row[4])
            ET.SubElement(order, "Date").text = row[5]

        tree = ET.ElementTree(root)
        tree.write("orders_export.xml")

        messagebox.showinfo(
            "Success",
            "Orders exported to XML successfully",
            parent=order_window
        )
    def create_order():
        if customer_combo.get() == "" or product_combo.get() == "" or quantity_entry.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=order_window)
            return

        customer_id = int(customer_combo.get().split(" - ")[0])
        product_id = int(product_combo.get().split(" - ")[0])
        price = float(product_combo.get().split("£")[1])
        quantity = quantity_entry.get()

        if not quantity.isdigit():
            messagebox.showerror(
                "Error",
                "Quantity must be a number",
                parent=order_window
            )
            return

        quantity = int(quantity)

        subtotal = price * quantity
        conn = sqlite3.connect("music store.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT StockQuantity
            FROM Products
            WHERE ProductID = ?
        """, (product_id,))

        stock = cursor.fetchone()[0]

        if quantity > stock:
            messagebox.showerror(
                "Error",
                "Not enough stock available",
                parent=order_window
            )
            conn.close()
            return
        cursor.execute("""
            INSERT INTO Orders (CustomerID, OrderDate, TotalAmount)
            VALUES (?, DATE('now'), ?)
        """, (customer_id, subtotal))

        order_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Subtotal)
            VALUES (?, ?, ?, ?)
        """, (order_id, product_id, quantity, subtotal))

        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Order created successfully", parent=order_window)

        quantity_entry.delete(0, tk.END)
        view_orders()


    create_order_button = tk.Button(
        order_window,
        text="Create Order",
        command=create_order,
        **button_style
    )
    create_order_button.pack(pady=10)
    load_data()
    view_orders_button = tk.Button(
        order_window,
        text="View Orders",
        command=view_orders,
        **button_style
    )

    view_orders_button.pack(pady=10)
    export_xml_button = tk.Button(
        order_window,
        text="Export Orders XML",
        command=export_orders_xml,
        **button_style
    )



    export_xml_button.pack(pady=10)

    def on_close():
        order_window.destroy()
        window.deiconify()
        window.state("zoomed")

    order_window.protocol("WM_DELETE_WINDOW", on_close)

# view customers fun
def view_customers():
    customer_table.pack(pady=20)

    conn = sqlite3.connect("music store.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Customers")
    rows = cursor.fetchall()

    customer_table.delete(*customer_table.get_children())

    for row in rows:
        customer_table.insert("", tk.END, values=row)

    conn.close()

# add fun
def add_customer():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if first_name == "" or last_name == "":
        messagebox.showerror("Error", "First name and last name required")
        return

    conn = sqlite3.connect("music store.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO Customers
        (FirstName, LastName, Email, Phone)
        VALUES (?, ?, ?, ?)
    """, (first_name, last_name, email, phone))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Customer added successfully")

    clear_fields()
    view_customers()

# clear fun
def clear_fields():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# fun select
def select_customer(event):
    selected = customer_table.focus()
    values = customer_table.item(selected, "values")

    if values:
        first_name_entry.delete(0, tk.END)
        first_name_entry.insert(0, values[1])

        last_name_entry.delete(0, tk.END)
        last_name_entry.insert(0, values[2])

        email_entry.delete(0, tk.END)
        email_entry.insert(0, values[3])

        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, values[4])

# upd fun
def update_customer():
    selected = customer_table.focus()
    values = customer_table.item(selected, "values")

    if not values:
        messagebox.showerror("Error", "Please select a customer")
        return

    customer_id = values[0]

    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if first_name == "" or last_name == "":
        messagebox.showerror("Error", "First name and last name required")
        return

    conn = sqlite3.connect("music store.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Customers
        SET FirstName = ?, LastName = ?, Email = ?, Phone = ?
        WHERE CustomerID = ?
    """, (first_name, last_name, email, phone, customer_id))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Customer updated successfully")

    view_customers()
    clear_fields()

# delete fun
def delete_customer():
    selected = customer_table.focus()
    values = customer_table.item(selected, "values")

    if not values:
        messagebox.showerror("Error", "Please select a customer")
        return

    customer_id = values[0]

    conn = sqlite3.connect("music store.db")
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM Customers
        WHERE CustomerID = ?
    """, (customer_id,))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Customer deleted successfully")

    view_customers()
    clear_fields()


def open_main_window():
    global window
    global first_name_entry, last_name_entry, email_entry, phone_entry
    global customer_table
    global button_style

    window = tk.Tk()
    window.title("Music Store Management System")
    window.state("zoomed")

    original_image = Image.open("images/Guitar.jpg")

    resized_image = original_image.resize((800, 600))
    bg_photo = ImageTk.PhotoImage(resized_image)

    background_label = tk.Label(window, image=bg_photo)
    background_label.image = bg_photo
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def resize_background(event):
        if event.widget == window:
            resized_image = original_image.resize((event.width, event.height))
            bg_photo = ImageTk.PhotoImage(resized_image)

            background_label.config(image=bg_photo)
            background_label.image = bg_photo

    window.bind("<Configure>", resize_background)

    button_style = {
        "bg": "#8B5A2B",
        "fg": "white",
        "font": ("Arial", 11, "bold"),
        "activebackground": "#A0522D",
        "activeforeground": "white",
        "bd": 3
    }

    title_label = tk.Label(
        window,
        text="Customer Management",
        font=("Arial", 18, "bold"),
        bg="#3E2723",
        fg="white"
    )
    title_label.pack(pady=10)

    first_name_label = tk.Label(
        window,
        text="First Name",
        bg="#BCAAA4",
        fg="black",
        font=("Arial", 10, "bold")
    )
    first_name_label.pack()

    first_name_entry = tk.Entry(window)
    first_name_entry.pack()

    last_name_label = tk.Label(
        window,
        text="Last Name",
        bg="#BCAAA4",
        fg="black",
        font=("Arial", 10, "bold")
    )
    last_name_label.pack()

    last_name_entry = tk.Entry(window)
    last_name_entry.pack()

    email_label = tk.Label(
        window,
        text="Email",
        bg="#BCAAA4",
        fg="black",
        font=("Arial", 10, "bold")
    )
    email_label.pack()

    email_entry = tk.Entry(window)
    email_entry.pack()

    phone_label = tk.Label(
        window,
        text="Phone",
        bg="#BCAAA4",
        fg="black",
        font=("Arial", 10, "bold")
    )
    phone_label.pack()

    phone_entry = tk.Entry(window)
    phone_entry.pack()

    add_button = tk.Button(
        window,
        text="Add Customer",
        command=add_customer,
        **button_style
    )
    add_button.pack(pady=10)

    view_button = tk.Button(
        window,
        text="View Customers",
        command=view_customers,
        **button_style
    )
    view_button.pack(pady=5)

    update_button = tk.Button(
        window,
        text="Update Customer",
        command=update_customer,
        **button_style
    )
    update_button.pack(pady=5)

    delete_button = tk.Button(
        window,
        text="Delete Customer",
        command=delete_customer,
        **button_style
    )
    delete_button.pack(pady=5)

    product_window_button = tk.Button(
        window,
        text="Open Product Management",
        command=open_product_window,
        **button_style
    )
    product_window_button.pack(pady=10)

    order_window_button = tk.Button(
        window,
        text="Open Order Management",
        command=open_order_window,
        **button_style
    )
    order_window_button.pack(pady=10)

    style = ttk.Style()
    style.theme_use("default")

    style.configure(
        "Custom.Treeview",
        background="#5C4033",
        foreground="white",
        fieldbackground="#5C4033",
        rowheight=32,
        font=("Arial", 10),
        borderwidth=2,
        relief="solid"
    )

    style.configure(
        "Custom.Treeview.Heading",
        background="#3E2723",
        foreground="white",
        font=("Arial", 11, "bold"),
        borderwidth=2,
        relief="solid"
    )

    style.map(
        "Custom.Treeview",
        background=[("selected", "#8B5A2B")]
    )

    customer_table = ttk.Treeview(
        window,
        columns=("ID", "First", "Last", "Email", "Phone"),
        show="headings"
    )

    customer_table.configure(height=8)
    customer_table["style"] = "Custom.Treeview"

    customer_table.heading("ID", text="ID")
    customer_table.heading("First", text="First Name")
    customer_table.heading("Last", text="Last Name")
    customer_table.heading("Email", text="Email")
    customer_table.heading("Phone", text="Phone")

    customer_table.bind("<ButtonRelease-1>", select_customer)

    window.mainloop()
login_screen()
