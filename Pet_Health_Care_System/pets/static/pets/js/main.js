<script>
      var dropdown = document.querySelector("#login_button .dropdown-menu");
      var isOpen = dropdown.classList.contains("show");
      if (isOpen) 
          dropdown.classList.remove("show");
      else
          dropdown.classList.add("show");
</script>