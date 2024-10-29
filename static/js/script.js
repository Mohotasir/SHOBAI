function togglePasswordVisibility(element) {
   const icon = element.children[0];
   const isPasswordVisible = icon.getAttribute("data-password") === "visible";

   // toggle eye icon
   icon.setAttribute("data-password", isPasswordVisible ? "hidden" : "visible");

   // toggle password input type
   const passwordInput = element.parentElement.querySelector(".password-field");
   passwordInput.type = isPasswordVisible ? "password" : "text";
}

function ShowUserMenu(element) {
   const menu = document.getElementById("account-details-menu");
   const isHidden = menu.classList.toggle("hidden");

   !isHidden
      ? document.addEventListener("click", hideOnClickOutside)
      : document.removeEventListener("click", hideOnClickOutside);

   function hideOnClickOutside(event) {
      if (!element.contains(event.target) && !menu.contains(event.target)) {
         menu.classList.add("hidden");
         document.removeEventListener("click", hideOnClickOutside);
      }
   }
}
