import React from 'react';
import styles from './CategoryForm.module.css';

const ProductList = ({ products, onDeleteProduct }) => {
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
                            <td>{product.category_name}</td>
                            <td>${product.price.toFixed(2)}</td>
                            <td>{product.stock}</td>
                            <td>
                                <button 
                                    onClick={() => onDeleteProduct(product.id)}
                                    className={styles.deleteButton}
                                >
                                    Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ProductList; 