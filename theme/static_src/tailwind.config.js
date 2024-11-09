/** @type {import('tailwindcss').Config} */
module.exports = {
   content: [
      "../../templates/**/*.html",
      "../../shobai/**/*.{html,py}",
      "../../apps/**/*.{html,py}",
   ],
   theme: {
      container: {
         center: true,
         padding: {
            DEFAULT: "1rem",
            sm: "1.5rem",
            lg: "2rem",
         },
         screens: {
            "2xl": "1400px",
         },
      },
      extend: {
         fontFamily: { sans: ["Mulish", "sans-serif"] },
         colors: {
            surface: "hsl(var(--surface))",
            background: "hsl(var(--background))",
            foreground: "hsl(var(--foreground))",
            border: "hsl(var(--border))",
            input: "hsl(var(--input))",
            ring: "hsl(var(--ring))",
            primary: {
               DEFAULT: "hsl(var(--primary))",
               foreground: "hsl(var(--primary-foreground))",
            },
            secondary: {
               DEFAULT: "hsl(var(--secondary))",
               foreground: "hsl(var(--secondary-foreground))",
            },
            destructive: {
               DEFAULT: "hsl(var(--destructive))",
               foreground: "hsl(var(--destructive-foreground))",
            },
            muted: {
               DEFAULT: "hsl(var(--muted))",
               foreground: "hsl(var(--muted-foreground))",
            },
            accent: {
               DEFAULT: "hsl(var(--accent))",
               foreground: "hsl(var(--accent-foreground))",
            },
            popover: {
               DEFAULT: "hsl(var(--popover))",
               foreground: "hsl(var(--popover-foreground))",
            },
         },
         borderRadius: {
            lg: "var(--radius)",
            md: "calc(var(--radius) - 2px)",
            sm: "calc(var(--radius) - 4px)",
         },
         boxShadow: {
            toast: "0 3px 10px rgba(0, 0, 0, 0.1), 0 3px 3px rgba(0, 0, 0, 0.05);",
            card: "0 0 12px 4px rgba(0, 0, 0, 0.05)",
         },
         keyframes: {
            "scale-in": {
               "0%": { opacity: 0, transform: "scale(0.5)" },
               "100%": { opacity: 1, transform: "scale(1)" },
            },
            "toast-appear": {
               from: { transform: "translate3d(0,-200%,0) scale(.6)", opacity: "0.5" },
               to: { transform: "translate3d(0,0,0) scale(1)", opacity: "1" },
            },
            "toast-scale-tick": {
               "0%": { height: "0", width: "0", opacity: "0" },
               "40%": { height: "0", width: "6px", opacity: "1" },
               "100%": { height: "10px", opacity: "1" },
            },
            "toast-scale-circle": {
               from: { transform: "scale(0) rotate(45deg)", opacity: "0" },
               to: { transform: "scale(1) rotate(45deg)", opacity: "1" },
            },
            "toast-scale-x-before": {
               from: { transform: "scale(0) rotate(90deg)", opacity: "0" },
               to: { transform: "scale(1) rotate(90deg)", opacity: "1" },
            },
            "toast-scale-x-after": {
               from: { transform: "scale(0)", opacity: "0" },
               to: { transform: "scale(1)", opacity: "1" },
            },
         },
         animation: {
            "scale-in": "scale-in 150ms cubic-bezier(0.2, 0, 0.13, 1.5) forwards",
            "toast-appear": "toast-appear 350ms cubic-bezier(0.21, 1.02, 0.73, 1) forwards",
            "toast-tick": "toast-scale-tick 200ms ease-out 200ms forwards",
            "toast-circle":
               "toast-scale-circle 300ms cubic-bezier(0.175,0.885,0.32,1.275) 100ms forwards",
            "toast-x-before": "toast-scale-x-before 150ms ease-out 180ms forwards",
            "toast-x-after": "toast-scale-x-after 150ms ease-out 150ms forwards",
         },
      },
   },
   plugins: [
      require("@tailwindcss/forms"),
      require("@tailwindcss/typography"),
      require("@tailwindcss/aspect-ratio"),
   ],
};
