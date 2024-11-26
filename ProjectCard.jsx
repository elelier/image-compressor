import React from 'react';
import './ProjectCard.css';

const ImageCompressorCard = () => {
  return (
    <div className="project-card">
      <div className="project-header">
        <h3>📸 Image Compressor</h3>
        <div className="project-tags">
          <span className="tag">Python</span>
          <span className="tag">PIL</span>
          <span className="tag">Image Processing</span>
        </div>
      </div>
      
      <p className="project-description">
        Una herramienta de compresión de imágenes que mantiene la calidad óptima
        mientras reduce el tamaño de archivo para correo electrónico y web.
      </p>
      
      <div className="project-features">
        <h4>Características principales:</h4>
        <ul>
          <li>✨ Compresión inteligente a menos de 1MB</li>
          <li>🎨 Mantiene la mejor calidad posible</li>
          <li>📁 Proceso por lotes de múltiples imágenes</li>
          <li>🔄 Soporta JPG, PNG, BMP y WEBP</li>
        </ul>
      </div>
      
      <div className="project-links">
        <a 
          href="https://github.com/TU_USUARIO/image-compressor" 
          target="_blank" 
          rel="noopener noreferrer"
          className="github-link"
        >
          Ver en GitHub
        </a>
      </div>
    </div>
  );
};

export default ImageCompressorCard;
