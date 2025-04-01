import streamlit as st

st.title("Order to Delivery Time Prediction")
st.header("Input Order Details")

product_category = st.selectbox("Product Category", 
                ["Electronics", "Clothing", "Home Appliances", "Books", "Other"])
customer_location = st.text_input("Customer Location")
shipping_method = st.selectbox("Shipping Method", 
                ["Standard", "Express", "Overnight"])


def predict_delivery_time(product_category, shipping_method):
    category_mapping = {"Electronics":0, "Clothing":1, 
                       "Home Appliances":2, "Books":3, "Other":4}
    shipping_mapping = {"Standard":0, "Express":1, "Overnight":2}
    
    return (category_mapping[product_category] 
           + shipping_mapping[shipping_method] 
           + 2)  # Simplified formula for demonstration

if st.button("Predict Delivery Time"):
    if customer_location:
        delivery_time = predict_delivery_time(product_category, shipping_method)
        st.success(f"Predicted delivery time: {delivery_time} days")
    else:
        st.error("Please enter a valid customer location")
