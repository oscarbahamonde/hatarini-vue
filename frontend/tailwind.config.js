module.exports = {
  content: [
    './**/**/*.{vue,js}',
  ],
  plugins: [require('daisyui')],
  
  daisyui:{
    themes: [{
      mytheme: {
          
        "primary": "#5BAA18",
                 
        "secondary": "#0AE9E5",
                 
        "accent": "#1C52B7",
                 
        "neutral": "#000000",
                 
        "base-100": "#f2f2f2",
                 
        "info": "#0C4B33",
                 
        "success": "#44B78B",
                 
        "warning": "#F24100",
                 
        "error": "#F1014E",
                 }
    }]
  }
}