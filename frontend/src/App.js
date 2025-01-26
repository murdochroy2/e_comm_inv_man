import React from 'react';
import ProductList from './components/ProductList';
import ProductForm from './components/ProductForm';
import './App.css';

function App() {
  const handleProductAdded = () => {
    // Force ProductList to reload
    window.location.reload();
  };

  return (
    <div className="App">
      <h1>Inventory Management System</h1>
      <ProductForm onProductAdded={handleProductAdded} />
      <ProductList />
    </div>
  );
}

export default App; 