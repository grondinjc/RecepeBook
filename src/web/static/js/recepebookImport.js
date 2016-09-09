function import_init() {
    var tmp = 'FULL RECIPE: http://bzfd.it/1TB2wKJ</span></a><div class="_2rm4"><div class="fsl fwn fcb"><span>Patricia Perreault-Paiement jen veux tout plein.</span><span role="presentation" aria-hidden="true"> · </span><abbr title="vendredi 11 mars 2016, 18:00" data-utime="1457737200"><span class="timestampContent">11 mars</span></abbr></div></div></div></div><div class="clearfix"><div class="_4bl7 _4bl8"><span class="_2n2m" id="u_17_1w"><span class="fcg">Enregistré à partir de <a class="_24-t" href="/veronique.charron.779/posts/10156588280210527">la publication de <span class="blueName">Véronique Charron</span></a></span></span></div><div class="_4bl9"><span class="_4-rr _4-rv"><a class="_42ft _4jy0 _4-rs _4-rt _4jy3 _517h _51sy" role="button" href="/ajax/sharer?appid=586254444758776&amp;p%5B0%5D=1725913947661247&amp;id=1725913947661247&amp;s=11" ajaxify="/ajax/sharer?appid=586254444758776&amp;p%5B0%5D=1725913947661247&amp;id=1725913947661247&amp;s=11" rel="dialog" id="u_17_v"><i class="_3-8_ img sp_pqLT_cIPtVz sx_5e86b1"></i>Partager</a></span></div></div></div></div><div class="clearfix _5wcf" id="u_17_f"><div class="_4bl7 _2l6b"><div id="u_17_g"><a class="_24-r" ajaxify="/ajax/flash/expand_inline.php?max_width=588&amp;override_360_width_as_max=1&amp;selector=%5E._5wcf&amp;target_div=u_17_g&amp;replace_target_div=1&amp;v=1723405201245455" href="/buzzfeedtasty/videos/1723405201245455/" rel="async"><span><img class="img" height="96" width="96" src="https://scontent-yyz1-1.xx.fbcdn.net/v/t15.0-10/p100x100/12514617_1723408614578447_1158178029_n.jpg?oh=ad65cb151c62749492d38a49e4cde0dc&amp;oe=57F09C26" alt=""></span><div class="_teu"></div></a></div></div><div class="_4bl9 _tev"><div class="clearfix _5wvh"><div class="_4bl7 _4bl8"><a class="_3a7p" ajaxify="/timeline/app/collection/item/curation/?collection_token=777067801%3A586254444758776%3A102&amp;object_id=1723405201245455&amp;action_type=add&amp;mechanism=xout_button&amp;surface=save_dashboard" rel="async-post" href="#" role="button" id="u_17_1p"><i class="_5voj img sp_-Avsn56WyAC sx_345971"></i></a></div><div class="_4bl9 _5yjp"><a href="/buzzfeedtasty/videos/1723405201245455/" target="_blank" id="u_17_19"><span class="_24-s">Cinnamon And Sugar Cheesecake Bars FULL RECIPE: http://bzfd.it/1QuP2Ky</span></a><div class="_2rm4"><div class="fsl fwn fcb"><span>Cinnamon And Sugar Cheesecake Bars FULL RECIPE: http://bzfd.it/1QuP2Ky</span><span role="presentation" aria-hidden="true"> · </span><abbr title="jeudi 3 mars 2016, 17:10" data-utime="1457043000"><span class="timestampContent">3 mars</span></abbr></div></div></div></div><div class="clearfix"><div class="_4bl7 _4bl8"><span class="_2n2m" id="u_17_1g"><span class="fcg">Enregistré à partir de <a class="_24-t" href="/buzzfeedtasty/videos/1723405201245455/">la publication de <span class="blueName">Tasty</span></a></span></span></div><div class="_4bl9"><span class="_4-rr _4-rv"><a class="_42ft _4jy0 _4-rs _4-rt _4jy3 _517h _51sy" role="button" href="/ajax/sharer?appid=586254444758776&amp;p%5B0%5D=1723405201245455&amp;id=1723405201245455&amp;s=11" ajaxify="/ajax/sharer?appid=586254444758776&amp;p%5B0%5D=1723405201245455&amp;id=1723405201245455&amp;s=11" rel="dialog" id="u_17_w"><i class="_3-8_ img sp_pqLT_cIPtVz sx_5e86b1"></i>Partager</a></span></div></div></div></div><div class="clearfix _5wcf" id="u_17_h"><div class="_4bl7 _2l6b"><div id="u_17_i"><a class="_24-r" ajaxify="/ajax/flash/expand_inline.php?max_width=588&amp;override_360_width_as_max=1&amp;selector=%5E._5wcf&amp;target_div=u_17_i&amp;replace_target_div=1&amp;v=1725250337727608" href="/buzzfeedtasty/videos/1725250337727608/" rel="async"><span><img class="img" height="96" width="96" src="https://scontent-yyz1-1.xx.fbcdn.net/v/t15.0-10/p100x100/12672742_1725253467727295_115805770_n.jpg?oh=757132c1725b560b30dd87626918df18&amp;oe=57EAE742" alt=""></span><div class="_teu"></div></a></div></div><div class="_4bl9 _tev"><div class="clearfix _5wvh"><div class="_4bl7 _4bl8"><a class="_3a7p" ajaxify="/timeline/app/collection/item/curation/?collection_token=777067801%3A586254444758776%3A102&amp;object_id=1725250337727608&amp;action_type=add&amp;mechanism=xout_button&amp;surface=save_dashboard" rel="async-post" href="#" role="button" id="u_17_1u"><i class="_5voj img sp_-Avsn56WyAC sx_345971"></i></a></div><div class="_4bl9 _5yjp"><a href="/buzzfeedtasty/videos/1725250337727608/" target="_blank" id="u_17_1a"><span class="_24-s">Homemade Passion Fruit Flan'
    
    var viewmodel = new ImportViewModel();
    ko.applyBindings(viewmodel);

    viewmodel.facebook_data(tmp);
}


// Overall viewmodel for this screen, along with initial state
function ImportViewModel() {
    var self = this;

    self.facebook_data = ko.observable();
    self.facebook_data_links = ko.observableArray();

    self.send_bookmark = function() {
        $.post("detect_bookmark_links", {
            bookmark_text: self.facebook_data()
        })
        .done(function(data, status) {
            alert("Data: " + data + "\nStatus: " + status);
            self.facebook_data_links($.parseJSON(data));
        })
        .fail(function(error) {
            alert("Error: " + error);
        });
    }
}
