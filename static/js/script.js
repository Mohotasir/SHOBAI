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

function showImage(e) {
   const imageInput = event.target;
   const preview = document.getElementById("image-preview");
   const file = imageInput.files[0];

   if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
         preview.src = e.target.result;
         preview.classList.remove("hidden");
      };
      reader.readAsDataURL(file);
   }
}
