import React, { useState } from 'react';
import styles from './CategoryForm.module.css';
import ProductUpdateModal from './ProductUpdateModal';

const ProductList = ({ products, onDeleteProduct, onUpdateProduct }) => {
    const [selectedProduct, setSelectedProduct] = useState(null);

    const handleUpdateClick = (product) => {
        setSelectedProduct(product);
    };

    const handleCloseModal = () => {
        setSelectedProduct(null);
    };

    return (
        <div className={styles.formContainer}>
            <h2>Products</h2>
            <table className={styles.productTable}>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Category</th>
                        <th>Price</th>
                        <th>Stock</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {products.map((product) => (
                        <tr key={product.id}>
                            <td>{product.name}</td>
                            <td>{product.category}</td>
                            <td>${(Number(product.price) || 0).toFixed(2)}</td>
                            <td>{product.quantity}</td>
                            <td>
                                <button 
                                    onClick={() => handleUpdateClick(product)}
                                    className={styles.editButton}
                                >
                                    Edit
                                </button>
                                <button 
                                    onClick={() => onDeleteProduct(product.sku)}
                                    className={styles.deleteButton}
                                >
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {selectedProduct && (
                <ProductUpdateModal
                    product={selectedProduct}
                    onClose={handleCloseModal}
                    onUpdate={onUpdateProduct}
                />
            )}
        </div>
    );
};

export default ProductList; 