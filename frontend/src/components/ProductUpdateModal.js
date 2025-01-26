import React, { useState } from 'react';
import styles from './CategoryForm.module.css';

const ProductUpdateModal = ({ product, onClose, onUpdate }) => {
    const [formData, setFormData] = useState({
        price: product.price || 0,
        quantity: product.quantity || 0
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await onUpdate(product.sku, {
                price: parseFloat(formData.price),
                quantity: parseInt(formData.quantity)
            });
            onClose();
        } catch (error) {
            alert('Error updating product');
        }
    };

    return (
        <div className={styles.modalOverlay}>
            <div className={styles.modalContent}>
                <h2>Update Product: {product.name}</h2>
                <form onSubmit={handleSubmit}>
                    <div className={styles.formGroup}>
                        <label htmlFor="price">Price:</label>
                        <input
                            type="number"
                            id="price"
                            name="price"
                            step="0.01"
                            value={formData.price}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className={styles.formGroup}>
                        <label htmlFor="quantity">Quantity:</label>
                        <input
                            type="number"
                            id="quantity"
                            name="quantity"
                            value={formData.quantity}
                            onChange={handleChange}
                            required
                        />
                    </div>
                    <div className={styles.modalButtons}>
                        <button type="submit" className={styles.updateButton}>Update</button>
                        <button type="button" onClick={onClose} className={styles.cancelButton}>Cancel</button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default ProductUpdateModal; 