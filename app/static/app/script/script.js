document.addEventListener("DOMContentLoaded", () => {
  const bars = document.querySelector(".navbar .fa-bars");
  const times = document.querySelector(".bar .fa-times");
  const bar = document.querySelector(".bar");

  bars.addEventListener("click", () => {
    bar.classList.add("show-bar");
  });

  times.addEventListener("click", () => {
    bar.classList.remove("show-bar");
  });

  const tajaupdatetimes = document.querySelector(".tajaupdate .fa-times");
  const tajaupdateicon = document.querySelector(".navbar .fa-clock");
  const tajaupdate = document.querySelector(".tajaupdate");

  tajaupdateicon.addEventListener("click", () => {
    tajaupdate.style.transform = "translateY(0px)";
    tajaupdate.style.transition = ".4s linear";
  });
  tajaupdatetimes.addEventListener("click", () => {
    tajaupdate.style.transform = "translateY(-2000px)";
    tajaupdate.style.transition = ".6s linear";
  });

  window.addEventListener("scroll", () => {
    const scrollTop = window.scrollY;
    if (scrollTop > 0) {
      tajaupdate.classList.add("sticky");
    } else {
      tajaupdate.classList.remove("sticky");
    }
  });


  window.addEventListener("scroll", () => {
    const scrollTop = window.scrollY;
    if (scrollTop > 0) {
      trend.classList.add("sticky");
    } else {
      trend.classList.remove("sticky");
    }
  });

  const trendtimesicon = document.querySelector(".trend .fa-times");
  const trendshareicon = document.querySelector(".navbar .fa-chart-line");
  const trend = document.querySelector(".trend");

  trendshareicon.addEventListener("click", () => {
    trend.style.transform = "translateY(0px)";
    trend.style.transition = ".4s linear";
    // body.style.filter = "blur(5px)";
  });
  trendtimesicon.addEventListener("click", () => {
    trend.style.transform = "translateY(-2000px)";
    trend.style.transition = ".6s linear";
  });
  // window.addEventListener("scroll", function () {
  //   const navbar = document.querySelector(".navbar");
  //   var stick = navbar.offsetTop;

  //   if (window.pageYOffset >= stick) {
  //     {
  //       navbar.classList.add("sticky");
  //       logo.classList.remove("hidden");
  //     }
  //   } else {
  //     navbar.classList.remove("sticky");
  //     logo.classList.add("hidden");
  //   }
  // });

  window.addEventListener("scroll", function () {
    const pag = document.querySelector(".bachat");
    var bachat = pag.offsetTop;
    if (window.pageYOffset >= bachat) {
      pag.classList.add("fix");
    } else {
      pag.classList.remove("fix");
    }
  });
});
