Vue.component("released-songs", {
  template: `
    <div>
        <h3>Title of the song</h3>
        <div>
            <iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/684781129&color=%230085ff&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>
        </div>
    </div>
    `,
});

var releaseApp = new Vue({
  el: "#release_section",
  data: {},
});
