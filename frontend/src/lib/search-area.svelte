<script lang="ts">
	import { laptops, searchCheckboxes, searchRanges, searchWords } from '../stores/results';
	import { getLaptops } from '../util/search';

	$: {
		(async () => {
			console.log($searchWords);
			$laptops = await getLaptops($searchCheckboxes, $searchRanges, $searchWords);
		})();
	}
</script>

<div>
	<input bind:value={$searchWords} placeholder="Search for laptop models here" />
</div>

<style>
	div {
		width: 100%;
		display: grid;
	}
	input {
		width: 80%;
		height: 50%;

		place-self: center left;

		border: none;
		border-radius: 5px;

		padding-left: 0.5rem;
	}
</style>
