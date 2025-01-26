import React, { useState, useEffect } from 'react';
import ProductForm from './ProductForm';
import ProductList from './ProductList';
import { productService } from '../services/api';

const ProductManagement = ({ categories }) => {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        loadProducts();
    }, []);

    const loadProducts = async () => {
        try {
            const data = await productService.getAllProducts();
            setProducts(data);
        } catch (error) {
            console.error('Error loading products:', error);
        }
    };

    const handleProductAdded = (newProduct) => {
        setProducts([...products, newProduct]);
    };

    const handleDeleteProduct = async (productId) => {
        try {
            await productService.deleteProduct(productId);
            setProducts(products.filter(prod => prod.id !== productId));
        } catch (error) {
            alert('Error deleting product');
        }
    };

    const handleUpdateProduct = async (productId, updateData) => {
        try {
            const updatedProduct = await productService.updateProduct(productId, updateData);
            setProducts(products.map(prod => 
                prod.id === productId ? updatedProduct : prod
            ));
        } catch (error) {
            alert('Error updating product');
        }
    };

    return (
        <div>
            <ProductForm 
                categories={categories} 
                onProductAdded={handleProductAdded} 
            />
            <ProductList 
                products={products} 
                onDeleteProduct={handleDeleteProduct}
                onUpdateProduct={handleUpdateProduct}
            />
        </div>
    );
};

export default ProductManagement; 